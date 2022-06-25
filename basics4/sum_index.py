def sum_func(some_str):
    x = 0
    for i in some_str:
        i = int(i)
        x += i
    return x

def sub_func(sum_num, some_str):
    y = 0
    while int(some_str) >= int(sum_num):
        some_str = int(some_str) - int(sum_num)
        print(some_str)


a = input(str())
print(sub_func(sum_func(a), a))

