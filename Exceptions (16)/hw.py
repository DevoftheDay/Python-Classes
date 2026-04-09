try:
    age = int(input("Enter your age here: "))

    if age <= 60:
        print("You are eligible.")
    else:
        print("You are not eligible.")
except ValueError:
    print("Invalid phrase")
