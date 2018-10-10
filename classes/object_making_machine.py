class Dog:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
#every function inside a class MUST have self as its first param!
    def bark(self):
        print('Woof, my name is', self.name, 'and Im', self.age, 'years old')

snooky = Dog('Snooky', 7)
snooky.bark()
