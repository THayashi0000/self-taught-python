class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length * 2 + self.width * 2

class Square:
    def __init__(self, l):
        self.length = l
    def calculate_perimeter(self):
        return self.length * 4

Rec = Rectangle(20, 40)
print(Rec.calculate_perimeter())
Squ = Square(30)
print(Squ.calculate_perimeter())
