import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, pv1: Point, pv2: Point):
        self.v = pv2.x - pv1.x
        self.w = pv2.y - pv1.y


class Triangle:
    def __init__(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3


def point_inside_triangle(p: Point, tr: Triangle):
    angle1 = evaluate_angle(Vector(p, tr.pt1), Vector(p, tr.pt2))
    angle2 = evaluate_angle(Vector(p, tr.pt1), Vector(p, tr.pt3))
    angle3 = evaluate_angle(Vector(p, tr.pt2), Vector(p, tr.pt3))

    return round(2*math.pi, 2) == round(angle1 + angle2 + angle3, 2)


def evaluate_angle(v1, v2: Vector):
    return math.acos(scalar_product(v1, v2)/(module(v1)*module(v2)))


def scalar_product(v1, v2 : Vector):
    return v1.v*v2.v+v1.w*v2.w


def module(v1: Vector):
    return math.sqrt(pow(v1.v, 2)+pow(v1.w, 2))


p = Point(2.5, 3)
tr = Triangle(Point(2, 1), Point(5, 3), Point(1, 6))
print(point_inside_triangle(p, tr))
