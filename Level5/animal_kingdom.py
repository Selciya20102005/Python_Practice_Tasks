class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def speak(self):
        print(f"{self.name} says Woof Woof!")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def speak(self):
        print(f"{self.name} says Meow Meow!")


animal = Animal("Animal", "Some Sound")
dog = Dog("Tommy")
cat = Cat("Kitty")

animal.speak()
dog.speak()
cat.speak()