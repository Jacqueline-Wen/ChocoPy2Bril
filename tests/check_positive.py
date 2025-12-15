# Function to check if a number is positive
def is_positive(n: int) -> bool:
    return n > 0

# Function to calculate sum and difference
def sum(a: int, b: int) -> int:
    return a + b
def diff(a: int, b: int) -> int:
    return a - b

x: int = 10
y: int = 4
flag: bool = True
i: int = 0
s: int = 0
d: int = 0

# Conditional
if flag and is_positive(x):
    print(True)
else:
    print(False)

# Call arithmetic function
s = sum(x, y)
d = diff(x, y)
print(s)
print(d)

# While loop
while i < 5:
    print(i)
    print(x * i)
    i = i + 1

# Logical operation
print(x > y or not flag)