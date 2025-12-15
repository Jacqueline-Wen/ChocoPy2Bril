def add(a: int, b: int) -> int:
    return a + b

x: int = 7
y: int = 3
active: bool = True
sum_val: int = 0
i: int = 0

if active and not x == y:
    print(False)
else:
    print(True)

sum_val = add(x, y)
print(sum_val)

while i < 3:
    print(i)
    print(x - i)
    i = i + 1