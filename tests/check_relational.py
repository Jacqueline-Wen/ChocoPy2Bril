def check_relational(x: int, y: int) -> bool:
    print(x == y)
    print(not (x == y))
    print(x < y)
    print(x <= y)
    print(x > y)
    print(x >= y)
    return True

def main(a: int, b: int) -> int:
    check: bool = True
    check = check_relational(a, b)
    return 0
