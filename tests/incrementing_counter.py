def inc(n: int) -> int:
    return n + 1

n: int = 0
i: int = 0
n = inc(n)
print(n == 1)
n = inc(n)
print(n == 2)
n = inc(n)
n = inc(n)
print(n == 4)

while i < 6:
    n = inc(n)
    i = i + 1
print(n == 10)
