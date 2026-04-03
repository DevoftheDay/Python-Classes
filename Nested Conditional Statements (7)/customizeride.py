print("Select your car")
print("1. Bike")
print("2. Car")

choice = int(input("Enter choice of vehicle here: "))

if(choice==1):
    print("What type of bike? ")
    print("1. Motorcycle")
    print("2. Scooter")
    choice2 = int(input("Enter your choice of bike here: "))
    if choice2==1:
        print("You have chosen a motorcycle." )
    else:
        print("You have chosen a scooter")

if(choice==2):
    print("What type of car? ")
    print("1. Sedan")
    print("2. SUV")
    choice3 = int(input("Enter what type of car here"))
    if choice3==1:
        print("You have chosen a sedan." )
    else:
        print("You have chosen a SUV")