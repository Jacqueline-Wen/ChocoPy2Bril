x: int = 1
y: int = 2
a: bool = True
b: bool = False

if a and True:
    print(True)
else:
    print(False)

if b or True:
    print(False)
else:
    print(True)

if x == y:
    print(True)
else:
    print(False)

if x == x:
    print(True)
else:
    print(False)
