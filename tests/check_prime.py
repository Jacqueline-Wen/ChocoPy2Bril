# Function to add and multiply two numbers
def add_and_multiply(a, b):
    return a + b, a * b

# Variables
x = 5        # int
y = 2        # int
active = True  # bool

# Conditional
if active and x > y:
    print(f"{x} is greater than {y} and active is True")
else:
    print(f"{x} is not greater than {y} or active is False")

# Arithmetic operations using function
sum_val, prod_val = add_and_multiply(x, y)
print(f"Sum: {sum_val}, Product: {prod_val}")

# While loop
i = 0
while i < 3:
    print(f"i = {i}, x + i = {x + i}")
    i += 1

# Logical operation
print(f"Is x > y or not active? {x > y or not active}")