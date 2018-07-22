class Square:
    recs = []

    def __init__(self, l):
        self.length = l
        self.recs.append(l)

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self, e):
        self.change_size = e
        self.length = self.length + self.change_size

    def print_size(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)

sq1 = Square(40)
sq2 = Square(60)
#print(Square.recs)
print(sq1.print_size())
