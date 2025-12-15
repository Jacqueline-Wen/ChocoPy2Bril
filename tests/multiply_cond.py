def multiply(a: int, b: int) -> int:
    return a * b

n: int = 5
limit: int = 4
show: bool = True

if show and n > 0:
    print("Multiplication table:")

i: int = 1
while i <= limit:
    print(n, "*", i, "=", multiply(n, i))
    i = i + 1