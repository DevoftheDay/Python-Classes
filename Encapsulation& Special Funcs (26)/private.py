class myClass:

    __privateVar = 27

    def __privateMet(self):
        print("I am inside the private method.")

    def callVar(self):
        print("Private variable = ", myClass.__privateVar)


foo = myClass()
foo.callVar()

#Calling private method makes an error occur
foo.__privateMet()