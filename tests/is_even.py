def is_even(n: int) -> bool:
    return n % 2 == 0

x: int = 8
y: int = 5

if is_even(x) and not is_even(y):
    print("x is even and y is odd")
else:
    print("x is not even or y is not odd")

i: int = 0
while i < 3:
    print("i =", i, "i % 2 == 0?", is_even(i))
    i = i + 1