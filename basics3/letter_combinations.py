from itertools import combinations


def comb(A):
    temp = combinations(A, 2)
    for i in list(temp):
        print(i)


comb(['a', 'e', 'i', 'o', 'u'])
