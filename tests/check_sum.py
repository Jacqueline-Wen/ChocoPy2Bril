def sum_and_check(a: int, b: int) -> bool:
    total: int = a + b
    return total > 10

x: int = 6
y: int = 5
active: bool = True

if active and sum_and_check(x, y):
    print("Active and sum > 10")
else:
    print("Inactive or sum <= 10")

i: int = 0
while i < 4:
    print("i =", i, "x * i =", x * i)
    i = i + 1

print("x >= y or not active?", x >= y or not active)