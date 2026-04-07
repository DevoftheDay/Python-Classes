def add(P,Q):
    return(P + Q)

def subtract(P,Q):
    return(P - Q)

def multiply(P,Q):
    return(P*Q)

def divide(P,Q):
    return(P/Q)

print("Please select the operation")
print("\na. Add \nb. Subtract \nc. Multiply \nd. Divide")
choice = input("Please enter your choice (a/b/c/d): ")

num1 = int(input("Please enter your first number here: "))
num2 = int(input("Please enter your second number here: "))

if choice == "a":
    print(num1, "+", num2, "=", (add(num1, num2)))
elif choice == "b":
    print(num1, "-", num2, "=", subtract(num1,num2))
elif choice == "c":
    print(num1, "*", num2, "=", multiply(num1,num2))
elif choice == "d":
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Error")