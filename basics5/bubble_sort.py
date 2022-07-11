my_list = [2, 1, 3, 5, 4]
f = int(1)

for j in my_list[0:-1]:
    for i in my_list[f:-1]:
        f += 1
        if j > i:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            print(my_list)
