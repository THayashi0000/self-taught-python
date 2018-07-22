class Shape:
    def what_am_i(self):
        return "I am a shpae"

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Shape):
    def __init__(self, l):
        self.length = l
    def calculate_perimeter(self):
        return self.length * 4

Rec = Rectangle(20, 40)
print(Rec.calculate_perimeter())
print(Rec.what_am_i())
Squ = Square(30)
print(Squ.calculate_perimeter())
