import math

class Circle:
    def __init__(self, r):
        self.radius = r
        self.area = int(r) * math.pi * 2
        print(self.area)

circle1 = Circle(10)
