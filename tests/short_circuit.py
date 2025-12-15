def foo() -> bool:
    print(False)
    return True


print(False or foo())
print(True and foo())
