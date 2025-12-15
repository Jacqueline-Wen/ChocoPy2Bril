def add(a: int, b: int) -> int:
    return a + b

x: int = 7
y: int = 3
active: bool = True

if active and x != y:
    print("x is not equal to y and active")
else:
    print("x equals y or inactive")

sum_val: int = add(x, y)
print("Sum:", sum_val)

i: int = 0
while i < 3:
    print("i =", i, "x - i =", x - i)
    i = i + 1