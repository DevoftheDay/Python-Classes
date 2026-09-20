from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk.")

class Snake(Animal):

    def move(self):
        print("I can slither.")

class Dog(Animal):
    def move(self):
        print("I can run.")

class Lion(Animal):
    def move(self):
        print("I can hunt.")

Obj = Human()
Obj.move()

Obj = Snake()
Obj.move()

Obj = Dog()
Obj.move()

Obj = Lion()
Obj.move()