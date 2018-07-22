class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Horse("Stanley", "Horse", mick)
print(stan.owner.name)
