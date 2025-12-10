import subprocess

# regenerating bril files for all tests
subprocess.run("for file in tests/*.py; do echo \"Running on $file\"; python3 chocopybril.py \"$file\"; done", shell=True)

# manually hard code test cases

# add_one.py
# assignment.py
# classes.py
# control_flow_2.py
# control_flow.py
# exponent.py
# expr_stmt.py
# globals.py
# hello_world.py
# incrementing_counter.py
# inherit_init.py
# int_and_bool_control_flow.py
# int_and_bool.py
# linked_list.py
# local_loop.py
# modulo.py
# nested_list.py
# null_and_empty_list_compare.py
# operators.py
# ratio.py
# short_circuit.py
# simple_list.py
# simple_string.py
# strings.py
# var_decl.py
