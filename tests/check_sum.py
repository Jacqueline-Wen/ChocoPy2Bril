def sum(a: int, b: int) -> int:
    return a + b

def check(a: int) -> bool:
    return a < 10

x: int = 3
y: int = 8
sum2: int = 0

sum2 = sum(x, y)
print(sum2)
print(check(sum2))