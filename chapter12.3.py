class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        self.area = int(b) * int(h) / 2
        print(self.area)

T = Triangle(10, 4)
