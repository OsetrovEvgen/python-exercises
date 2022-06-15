import math


def circle_area(r):
    area = math.pi * math.pow(r, 2)
    return area


print(circle_area(int(input())))
