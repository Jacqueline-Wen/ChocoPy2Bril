def operations(a: int, b: int) -> [int]:
    return [a + b, a * b, a / b, a - b]

x: int = 12
y: int = 4
active: bool = True

if x >= y or not active:
    print("x is greater or equal to y or inactive")

results: [int] = operations(x, y)
print("Add, Mul, Div, Sub:", results)

i: int = 0
while i < 3:
    print("i =", i)
    i = i + 1