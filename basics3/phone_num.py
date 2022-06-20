def phone_num(first_set, second_set):
    return first_set.difference(second_set)


first_set = set(input())
second_set = set(input())
print(phone_num(first_set, second_set))

