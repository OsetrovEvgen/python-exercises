a = [1, 2, 3, -2, 0, -4]

for i in a:
    for j in a:
        for k in a:
            if sum((i, j, k)) == 0:
                print(i, j, k)


