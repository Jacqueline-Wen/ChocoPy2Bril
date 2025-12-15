def multiply(a: int, b: int) -> int:
    return a * b

def cond(a: int, b: int, limit: int) -> bool:
    if a > b:
        return (a - b) < limit
    return (b - a) < limit

x: int = 5
y: int = 7
z: int = 3
limit: int = 4

res1: int = 0
res2: int = 0
res1 = multiply(x, y)
res2 = multiply(y, z)
print(res1)
print(res2)
print(cond(res1, res2, limit))