import itertools
import datetime
import time


def factorial(n, start, step):
    result = 1
    iter_num = itertools.count(start=start, step=step)
    for i in iter_num:
        time.sleep(0.5)
        result *= i
    return result


res = factorial(2, 1, 1)

