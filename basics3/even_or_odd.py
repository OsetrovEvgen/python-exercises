
def even_odd(x, y):
    if x % 2 == 0:
        print(y, ' + ', x, ' = ', y / x , '', '- делитель чётное число')
    else:
        print(y, ' + ', x, ' = ', y / x , '', '- делитель не чётное число')


x = int(input())
y = int(input())
even_odd(x, y)
