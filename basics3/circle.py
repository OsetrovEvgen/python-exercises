import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius, center: Point):
        self.radius = radius
        self.center = center

    def has_inside(self, c):
        return distance_center(self.center, c.center) <= (self.radius - c.radius)


def distance_center(p1, p2: Point):
    return math.sqrt(pow(p2.x - p1.x, 2) + (pow(p2.y - p1.y, 2)))


print(distance_center(Point(2, 3), Point(4, 5)))
c = Circle(4, Point(2, 3))
print(c.has_inside(Circle(8, Point(2, 3))))
