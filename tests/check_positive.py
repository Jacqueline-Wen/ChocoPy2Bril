# Function to check if a number is positive
def is_positive(n: int) -> bool:
    return n > 0

# Function to calculate sum and difference
def sum_and_diff(a: int, b: int) -> [int]:
    return [a + b, a - b]

x: int = 10
y: int = 4
flag: bool = True

# Conditional
if flag and is_positive(x):
    print("x is positive and flag is True")
else:
    print("x is not positive or flag is False")

# Call arithmetic function
results: [int] = sum_and_diff(x, y)
print("Sum and Difference:", results)

# While loop
i: int = 0
while i < 5:
    print("i =", i, "x * i =", x * i)
    i = i + 1

# Logical operation
print("x > y or not flag?", x > y or not flag)