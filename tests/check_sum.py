def sum(a: int, b: int) -> int:
    return a + b

def check(a: int) -> bool:
    return a < 10

x: int = 3
y: int = 8
sum: int = 0

sum = sum(x, y)
print(sum)
print(check(sum))