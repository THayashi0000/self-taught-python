class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6

Hexagon = Hexagon(10)
print(Hexagon.calculate_perimeter())
