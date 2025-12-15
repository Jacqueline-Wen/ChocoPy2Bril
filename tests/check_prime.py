def is_prime(n: int, i: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n - (2 * (n // 2)) == 0:
        return False
    while i * i <= n:
        if n - (i * (n // i)) == 0:
            return False
        i = i + 2
    return True

def main(a: int) -> int:
    b: bool = False     # declaration must come before statements
    i: int = 3
    b = is_prime(a, i)
    print(b)
    return 0        # ChocoPy requires functions to return if typed non-void
