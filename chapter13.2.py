class Square:
    def __init__(self, l):
        self.length = l
    def calculate_perimeter(self):
        return self.length * 4
    def change_size(self, e):
        self.change_size = e
        self.length = self.length + self.change_size

Squ = Square(30)
Squ.change_size(-10)
print(Squ.calculate_perimeter())
