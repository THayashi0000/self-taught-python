class Apple:
    def __init__(self, w, c, size, l):
        self.w = w
        self.colour= c
        self.size = size
        self.length = l
        print("Created")

Ap1 = Apple(100, "dark red", 50, 40)
print(Ap1.size)
