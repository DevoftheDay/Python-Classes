class IOString():

    def __init__(self):
        self.str1 = ""


    def get_String(self):
        self.str1 = input("Enter a string here: ")

    def print_String(self):
        print("Result is: ", self.str1.upper())


#create object
str1 = IOString()

#call function
str1.get_String()
str1.print_String()