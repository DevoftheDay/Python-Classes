class Dog:
    color = "brown"

    def __init__(self,name,age):
        self.name = name
        self.age = age

ned = Dog('Ned', 7)
walt = Dog('Walt', 4)

print("The color of ned is: ", ned.color)
print("The color of walt is: ", walt.color)
print("{} is {} years old".format(ned.name, ned.age))
print("{} is {} years old".format(walt.name, walt.age))