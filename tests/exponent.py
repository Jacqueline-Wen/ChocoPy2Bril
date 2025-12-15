def f(i: int, x: int, a: int) -> int:
    if i <= 0:
        return a
    else:
        a = a * x
        return f(i-1, x, a)

# Compute x**y
def exp(x: int, y: int) -> int:
    a: int = 1
    return f(y, x, a)


# Input parameter
n: int = 42

# Run [0, n]
i: int = 0
exponent_val: int = 0

# Crunch
while i <= n:
    print(exp(2, exponent_val))
    i = i + 1
    if exponent_val == 30:
        exponent_val = 0
    else:
        exponent_val = exponent_val + 1

print(exp(2, 3) == 8)
print(exp(3, 3) == 27)
print(exp(3, 4) == 81)
print(exp(4, 4) == 256)
print(exp(5, 1) == 5)
print(exp(1, 99) == 1)
