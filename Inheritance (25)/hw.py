class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_traits(self):
        print("Brand: ", self.brand)
        print("Max Speed: ", self.max_speed)


class Car(Vehicle):

    def __init__(self, name, age, brand, max_speed):
        self.name = name
        self.age = age
        super().__init__(brand, max_speed)

    def show_traits(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().show_traits()
        


child = Car("Prius", 30, "Toyota", "180 mph")

child.show_traits()

print("Car is subclass of vehicle??", issubclass(Car, Vehicle))