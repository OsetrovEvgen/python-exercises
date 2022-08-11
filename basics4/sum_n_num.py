def some_funk(a, b):
    # a = int(a)
    b = int(b)
    x = sum([int(i) for i in list(str(a[:b]))])
    return x


print(some_funk(input(), input()))
