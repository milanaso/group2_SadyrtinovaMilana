import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x+1
        self.y = y+1

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


point1 = Point(0, 0)
point2 = Point(3, 4)

point1.show()
point2.show()

print(point1.dist(point2))

point1.move(1, 1)
point1.show()
