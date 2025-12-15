x: int = 0
z: int = 0


def t(x: int, z: int) -> int:
    x = x + 1
    z = z + z
    print(z == 0)
    return x


print(x == 0)
x = t(x, z)
print(x == 1)