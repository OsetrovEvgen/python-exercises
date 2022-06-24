def dif_int(a):
    if a.isnumeric() == False:
        print('Enter a valid number')
    x = ''.join(sorted(a))
    y = ''.join(sorted(a, reverse=True))
    x = int(x)
    y = int(y)
    z = y - x
    return z


print(dif_int(input()))
