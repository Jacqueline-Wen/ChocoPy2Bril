import subprocess
import io
from contextlib import redirect_stdout
import random

buf = io.StringIO()
with redirect_stdout(buf):
    import tests.add_one

# regenerating bril files for all tests
# subprocess.run("for file in tests/*.py; do echo \"Running on $file\"; python3 chocopybril.py \"$file\"; done", shell=True)

# Test 1: add_one.py
print("[Test 1] Starting to process add_one")
rnum = random.randint(1, 10)
bril_result = subprocess.run(
    f"brili {rnum} < tests/add_one.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

buf = io.StringIO()
with redirect_stdout(buf):
    tests.add_one.main(rnum)

py_output = buf.getvalue().strip()
print("chocopy ", py_output)

assert(bril_output == py_output)
print("[Test 1] add_one test successful\n")

# Test 2: assignment.py
print("[Test 2] Starting to process assignment")
bril_result = subprocess.run(
    "brili < tests/assignment.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/assignment.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 2] assignment test successful\n")

# Test3: control_flow_2.py
print("[Test 3] Starting to process control flow 2")
bril_result = subprocess.run(
    "brili < tests/control_flow_2.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/control_flow_2.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 3] control flow 2 test successful\n")

# Test 4: exponent.py
print("[Test 4] Starting to process exponent")
bril_result = subprocess.run(
    "brili < tests/exponent.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/exponent.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 4] exponent test successful\n")

# Test 5: expr_stmt.py
print("[Test 5] Starting to process expr_stmt")
bril_result = subprocess.run(
    "brili < tests/expr_stmt.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/expr_stmt.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 5] expr_stmt test successful\n")

# hello_world.py
print("[Test 6] Starting to process hello_world")
bril_result = subprocess.run(
    "brili < tests/hello_world.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/hello_world.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 6] hello_world test successful\n")

# incrementing_counter.py
print("[Test 7] Starting to process incrementing_counter")
bril_result = subprocess.run(
    "brili < tests/incrementing_counter.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/incrementing_counter.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 7] incrementing_counter test successful\n")

# Test 8: int_and_bool_control_flow.py
print("[Test 8] Starting to process int_and_bool_control_flow")
bril_result = subprocess.run(
    "brili < tests/int_and_bool_control_flow.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/int_and_bool_control_flow.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 8] int_and_bool_control_flow test successful\n")

# int_and_bool.py
print("[Test 9] Starting to process int_and_bool")
bril_result = subprocess.run(
    "brili < tests/int_and_bool.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/int_and_bool.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 9] int_and_bool test successful\n")

# local_loop.py
print("[Test 10] Starting to process local_loop")
bril_result = subprocess.run(
    "brili < tests/local_loop.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/local_loop.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 10] local_loop test successful\n")

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
