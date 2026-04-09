try:
    number = int(input("Enter a number here: "))
    print("The number is", number)

except ValueError as x:
    print("Exception", x)