class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, pv1, pv2):
        self.pv1 = pv1
        self.pv2 = pv2


class Triangle:
    def __init__(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3

def evaluate_angle(v1,v2):




p1 = Point(2, 1)
p2 = Point(6, 1)
p3 = Point(5, 3)

tr = Triangle(p1, p2, p3)
print(tr.pt1.x)



