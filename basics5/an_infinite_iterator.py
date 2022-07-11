import itertools
import datetime
import time


def iter_funk(start, step):
    iter_num = itertools.count(start=start, step=step)
    x = []
    for i in iter_num:
        x.append(i)
        if i >= 30:
            break
    return x


print(iter_funk(3, 5))
