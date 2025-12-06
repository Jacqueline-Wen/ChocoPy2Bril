import ast
import subprocess
import sys

def chocopy_ast(file_path):
    subprocess.run(["python", "chocopy-python-compiler/main.py", "--mode", "parse", file_path, "tests"])    

if __name__ == "__main__":
    file_path = sys.argv[1]
    chocopy_ast(file_path)

    ast_file_path = file_path[:-2] + "ast"
    