class Dog:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
#every function inside a class MUST have self as its first param!
    def bark(self):
        print('Woof, my name is', self.name, 'and Im', self.age, 'years old')

snooky = Dog('Snooky', 7)
snooky.bark()


class WaterGlass:
    def __init__(self, capacity, amount=0):
        self.capacity = capacity
        self.amount = amount
    def empty(self):
        self.amount = 0
    def fill(self):
        self.amount = self.capacity
    def drink(self):
        self.amount -= 1

marias_glass = WaterGlass(12)
print("maria's glass has", marias_glass.amount, "oz")
marias_glass.fill()
print("maria's glass has", marias_glass.amount, "oz")
