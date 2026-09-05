class Animal:
    def __init__(self, name):   #construtor
        self.name = name

    def sound(self):            #method
        print(self.name, "makes a sound")


class Dog(Animal):           #inheritance          
    def sound(self):
        print(self.name, "barks")


d = Dog("Tommy")
d.sound()