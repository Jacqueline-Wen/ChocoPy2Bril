def add_one(x: int) -> int:
    return x + 1

def main(a: int) -> int:
    b: int = 0      # declaration must come before statements
    b = add_one(a)
    print(b)
    return 0        # ChocoPy requires functions to return if typed non-void
