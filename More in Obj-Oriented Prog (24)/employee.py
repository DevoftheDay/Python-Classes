class Employee:

    def __init__(self):
        print("Employee created.")

    def __del__(self):
        print("Destructor called.")


def create_Obj():
    print("Making object.")
    Obj = Employee()
    print("End of function")
    return Obj

print("Calling create_Obj function.")
Obj = create_Obj()
print("Program end.")