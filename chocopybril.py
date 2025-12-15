import ast
import subprocess
import sys
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field

class CodeState:
    def __init__(self, func_ret_types):
        self.temp = 0
        self.label = 0
        self.var_types = {}
        self.func_ret_types = func_ret_types

    def make_temp(self, type):
        name = "_temp"+str(self.temp)
        self.temp += 1
        self.var_types[name] = type
        return name
    
    def make_label(self, type):
        name = type+"_"+str(self.label)
        self.label+=1
        return name
    
UNARY_OP = {
    "not": "not",
}

BIN_OP = {
    "+": "add",
    "-": "sub",
    "*": "mul",
    "//": "div",
    "==": "eq",
    "<": "lt",
    "<=": "le",
    ">": "gt",
    ">=": "ge",
    "and": "and",
    "or": "or",
}

def chocopy_ast(file_path):
    subprocess.run(["python", "chocopy-python-compiler/main.py", "--mode", "parse", file_path, "tests"])    

def translate_prog(ast_dict):
    declarations = ast_dict.get("declarations", [])
    statements = ast_dict.get("statements", [])

    func_ret_types = {}
    for d in declarations:
        if d.get("kind") == "FuncDef":
            func_name = d["name"]["name"]
            func_ret = d.get("returnType",{}).get("className", None)
            func_ret_types[func_name] = func_ret
    
    functions = []
    global_vardefs = [d for d in declarations if d.get("kind") == "VarDef"]

    #function declarations
    for d in declarations:
        kind = d.get("kind")
        if kind == "FuncDef":
            functions.append(translate_func_def(d, func_ret_types)) #ignore classdef

    
    #building main
    if global_vardefs or statements:
        state = CodeState(func_ret_types=func_ret_types)
        instrs = []
        
        for gv in global_vardefs:
            instrs.extend(translate_var_def(gv, state))
        for stmt in statements:
            instrs.extend(translate_stmt(stmt, state))
        if not instrs or instrs[-1].get("op") != "ret":
            instrs.append({"op": "ret"})
        functions.append(
            {
                "name": "main",
                "args": [],
                "instrs": instrs,
                "type": None,
            }
        )
    return {"functions": functions}


def translate_func_def(f, func_ret_types):
    s = CodeState(func_ret_types)
    func_name = f["name"]["name"]
    args = []
    for param in f.get("params",[]):
        var_name = param["identifier"]["name"]
        var_type = param["type"]["className"]
        args.append({"name": var_name, "type": var_type})
        s.var_types[var_name] = var_type
    
    instrs = []
    for decl in f.get("declarations", []):
        if decl.get("kind") == "VarDef":
            instrs.extend(translate_var_def(decl, s))
    for stmt in f.get("statements", []):
        instrs.extend(translate_stmt(stmt, s))

    ret_type = f.get("returnType", {}).get("className", None)
    # print(ret_type)
    if not instrs or instrs[-1].get("op") != "ret":
        if ret_type is None:
            instrs.append({"op": "ret"})
        else:
            if ret_type == "int":
                t0 = s.make_temp("int")
                instrs.append(
                    {"op": "const", "dest": t0, "type": "int", "value": 0}
                )
                instrs.append({"op": "ret", "args": [t0]})
            elif ret_type == "bool":
                t0 = s.make_temp("bool")
                instrs.append(
                    {"op": "const", "dest": t0, "type": "bool", "value": False}
                )
                instrs.append({"op": "ret", "args": [t0]})

    ret = {
        "name": func_name,
        "args": args,
        "instrs": instrs,
    }
    # print("this is ret type", str(ret_type))
    if ret_type and ret_type != "<None>":
        ret["type"] = ret_type
    return ret

def translate_var_def(vardef, state):
    var_name = vardef["var"]["identifier"]["name"]
    var_type = vardef["var"]["type"]["className"]
    state.var_types[var_name] = var_type

    instrs = []
    v_tmp, v_type, v_instrs = translate_expr(vardef["value"], state)
    instrs.extend(v_instrs)
    instrs.append(
        {
            "op": "id",
            "dest": var_name,
            "type": var_type,
            "args": [v_tmp],
        }
    )
    return instrs

def is_print_call(expr):
    if expr.get("kind") != "CallExpr":
        return False
    return expr["function"]["kind"]=="Identifier" and expr["function"]["name"] == "print"

def translate_expr(expr, state):
    kind = expr.get("kind")
    print(expr, kind)

    if kind == "IntegerLiteral":
        temp = state.make_temp("int")
        instr = [
            {"op": "const", "dest": temp, "type": "int", "value": expr["value"]}
        ]
        return temp, "int", instr
    elif kind == "BooleanLiteral":
        temp = state.make_temp("int")
        instr = [
            {"op": "const", "dest": temp, "type": "bool", "value": bool(expr["value"])}
        ]
        return temp, "bool", instr
    elif kind == "Identifier":
        name = expr["name"]
        typ = state.var_types.get(name, "int")
        temp = state.make_temp(typ)
        instrs = [{"op": "id", "dest": temp, "type": typ, "args": [name]}]
        return temp, typ, instrs
    elif kind == "UnaryExpr":
        operand = expr["operand"]
        op = expr["operator"]
        op_tmp, op_type, op_instrs = translate_expr(operand, state)
        instrs = op_instrs
        if op == '-':
            if op_type != 'int':
                raise TypeError("Unary minus only supported for integer type.")
            result_type = 'int'
            tmp = state.make_temp(result_type)
            v_zero = state.make_temp('int')
            instrs.append({
                "op": "const",
                "dest": v_zero,
                "type": "int",
                "value": 0
            })
            instrs.append({
                "op": "sub",
                "dest": tmp,
                "type": result_type,
                "args": [v_zero, op_tmp],
            })
            return tmp, result_type, instrs
        
        bril_op = UNARY_OP.get(op)
        if bril_op is None:
            raise NotImplementedError(f"Unary op not supported: {op}")
        if bril_op == "neg":
            result_type = "int"
        elif bril_op == "not":
            result_type = "bool"
        else:
            result_type = op_type
        tmp = state.make_temp(result_type)
        instrs.append(
            {
                "op": bril_op,
                "dest": tmp,
                "type": result_type,
                "args": [op_tmp],
            }
        )
        return tmp, result_type, instrs
    elif kind == "BinaryExpr":
        left = expr["left"]
        right = expr["right"]
        op = expr["operator"]

        l_tmp, l_type, l_instrs = translate_expr(left, state)
        r_tmp, r_type, r_instrs = translate_expr(right, state)
        instrs = l_instrs + r_instrs

        bril_op = BIN_OP.get(op)
        if bril_op is None:
            raise NotImplementedError(f"Binary op not supported: {op}")

        if bril_op in ("add", "sub", "mul", "div", "mod"):
            result_type = "int"
        else:
            result_type = "bool"

        tmp = state.make_temp(result_type)
        instrs.append(
            {
                "op": bril_op,
                "dest": tmp,
                "type": result_type,
                "args": [l_tmp, r_tmp],
            }
        )
        return tmp, result_type, instrs
    elif kind == "CallExpr":
        func_name = expr["function"]["name"]
        arg_temps = []
        instrs = []
        for a in expr.get("args", []):
            t, t_type, t_instrs = translate_expr(a, state)
            instrs.extend(t_instrs)
            arg_temps.append(t)
        ret_type = state.func_ret_types.get(func_name, "int")
        temp = state.make_temp(ret_type)
        instrs.append(
            {
                "op": "call",
                "funcs": [func_name],
                "args": arg_temps,
                "dest": temp,
                "type": ret_type
            }
        )
        return temp, ret_type, instrs
    
    raise NotImplementedError(f"Expression kind not supported yet {kind}")

def translate_stmt(stmt, state):
    kind = stmt.get("kind")
    instrs = []

    if kind == "AssignStmt":
        target = stmt["targets"][0]
        var_name = target["name"]
        v_tmp, v_type, v_instrs = translate_expr(stmt["value"], state)
        instrs.extend(v_instrs)
        var_type = state.var_types.get(var_name, v_type)
        state.var_types[var_name] = var_type
        instrs.append(
            {
                "op": "id",
                "dest": var_name,
                "type": var_type,
                "args": [v_tmp],
            }
        )
        return instrs
    elif kind == "IfStmt":
        cond_tmp, _, cond_instrs = translate_expr(stmt["condition"], state)
        instrs.extend(cond_instrs)

        then_label = state.make_label("then")
        else_label = state.make_label("else")
        end_label = state.make_label("endif")

        instrs.append(
            {"op": "br", "args": [cond_tmp], "labels": [then_label, else_label]}
        )

        # then
        instrs.append({"label": then_label})
        for s in stmt.get("thenBody", []):
            instrs.extend(translate_stmt(s, state))
        instrs.append({"op": "jmp", "labels": [end_label]})

        # else block
        instrs.append({"label": else_label})
        for s in stmt.get("elseBody", []):
            instrs.extend(translate_stmt(s, state))
        instrs.append({"op": "jmp", "labels": [end_label]})

        instrs.append({"label": end_label})
        return instrs
    elif kind == "WhileStmt":
        header_label = state.make_label("while_header")
        body_label = state.make_label("while_body")
        end_label = state.make_label("while_end")
        instrs.append({"op": "jmp", "labels": [header_label]})
        instrs.append({"label": header_label})
        cond_tmp, _, cond_instrs = translate_expr(stmt["condition"], state)
        instrs.extend(cond_instrs)
        instrs.append(
            {"op": "br", "args": [cond_tmp], "labels": [body_label, end_label]}
        )
        instrs.append({"label": body_label})
        for s in stmt.get("body", []):
            instrs.extend(translate_stmt(s, state))
        instrs.append({"op": "jmp", "labels": [header_label]})
        instrs.append({"label": end_label})
        return instrs
    elif kind == "ReturnStmt":
        value = stmt.get("value")
        if value is None:
            instrs.append({"op": "ret"})
        else:
            v_tmp, v_type, v_instrs = translate_expr(value, state)
            instrs.extend(v_instrs)
            instrs.append({"op": "ret", "args": [v_tmp]})
        return instrs
    if kind == "ExprStmt":
        expr = stmt["expr"]
        if expr.get("kind") == "CallExpr" and is_print_call(expr):
            arg_temps= []
            for a in expr.get("args", []):
                t, t_type, t_instrs = translate_expr(a, state)
                instrs.extend(t_instrs)
                arg_temps.append(t)
            instrs.append({"op": "print", "args": arg_temps})
            return instrs
        else:
            _, _, e_instrs = translate_expr(expr, state)
            instrs.extend(e_instrs)
            return instrs
    
    raise NotImplementedError(f"Statement kind not supported yet: {kind}")
    
if __name__ == "__main__":
    file_path = sys.argv[1]
    chocopy_ast(file_path)

    ast_file_path = file_path[:-2] + "ast"
    with open(ast_file_path, "r") as f:
        ast_dict = json.load(f)
    bril_prog = translate_prog(ast_dict)

    json_file_path = file_path[:-2]+"json"
    with open(json_file_path, "w") as f:
        json.dump(bril_prog, f, indent=2)

    bril_file_path = file_path[:-2]+"bril"
    cmd = f"bril2txt < {json_file_path} > {bril_file_path}"
    subprocess.run(cmd, shell=True, check=True)