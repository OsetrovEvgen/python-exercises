def some_func(x, y):
    a = list()
    for i in range(1, 10):
        if x % i == 0:
            if y % i == 0:
                a.append(i)
    return a


x = 18
y = 72

print(some_func(x, y))
