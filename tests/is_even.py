def is_even(n: int) -> bool:
    half = n // 2
    return n == half * 2

x: int = 8
y: int = 5

is_even_x: bool = False
is_even_y: bool = False
is_even_x = is_even(x)
is_even_y = is_even(y)
print(is_even_x)
print(is_even_y)