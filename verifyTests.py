import subprocess
import io
from contextlib import redirect_stdout
import random

buf = io.StringIO()
with redirect_stdout(buf):
    import tests.add_one
    import tests.check_prime
    import tests.check_relational

# regenerating bril files for all tests
subprocess.run("for file in tests/*.py; do echo \"Running on $file\"; python3 chocopybril.py \"$file\"; done", shell=True)

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

# Test 9: int_and_bool.py
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

# Test 10: local_loop.py
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

# Test 11: operators.py
print("[Test 11] Starting to process operators")
bril_result = subprocess.run(
    "brili < tests/operators.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/operators.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 11] operators test successful\n")

# Test 12: short_circuit.py
print("[Test 12] Starting to process short_circuit")
bril_result = subprocess.run(
    "brili < tests/short_circuit.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/short_circuit.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 12] short_circuit test successful\n")

# Test 13: var_decl.py
print("[Test 13] Starting to process var_decl")
bril_result = subprocess.run(
    "brili < tests/var_decl.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/var_decl.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 13] var_decl test successful\n")

# Test 14: basic_arithmetic.py
print("[Test 14] Starting to process basic_arithmetic")
bril_result = subprocess.run(
    "brili < tests/basic_arithmetic.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/basic_arithmetic.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 14] basic_arithmetic test successful\n")

# Test 15: check_positive.py
print("[Test 15] Starting to process check_positive")
bril_result = subprocess.run(
    "brili < tests/check_positive.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/check_positive.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 15] check_positive test successful\n")

# Test 16: check_prime.py
print("[Test 16] Starting to process check_positive")
rnum = random.randint(1, 100)
bril_result = subprocess.run(
    f"brili {rnum} < tests/check_prime.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

buf = io.StringIO()
with redirect_stdout(buf):
    tests.check_prime.main(rnum)

py_output = buf.getvalue().strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 16] check_prime test successful\n")

# Test 17: check_relational.py
print("[Test 17] Starting to process check_relational")
rnum = random.randint(1, 100)
rnum2 = random.randint(1, 100)
bril_result = subprocess.run(
    f"brili {rnum} {rnum2} < tests/check_relational.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

buf = io.StringIO()
with redirect_stdout(buf):
    tests.check_relational.main(rnum, rnum2)

py_output = buf.getvalue().strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 17] check_relational test successful\n")

# Test 18: check_sum.py
print("[Test 18] Starting to process check_sum")
bril_result = subprocess.run(
    "brili < tests/check_sum.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/check_sum.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 18] check_sum test successful\n")

# Test 19: is_even.py
print("[Test 19] Starting to process is_even")
bril_result = subprocess.run(
    "brili < tests/is_even.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/is_even.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 19] is_even test successful\n")

# Test 20: multiply_cond.py
print("[Test 20] Starting to process multiply_cond")
bril_result = subprocess.run(
    "brili < tests/multiply_cond.json",
    shell=True,
    capture_output=True,
    text=True
)

bril_output = bril_result.stdout
bril_output = bril_result.stdout.strip()
print("bril ", bril_output)

py_result = subprocess.run(
    "python3 tests/multiply_cond.py",
    shell=True,
    capture_output=True,
    text=True
)

py_output = py_result.stdout
py_output = py_result.stdout.strip()
print("chocopy ", py_output)

assert(bril_output.strip().lower() == py_output.strip().lower())
print("[Test 20] multiply_cond test successful\n")