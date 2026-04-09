try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by 0 is an error.")

except SyntaxError:
    print("A comma is missing. Enter two numbers seperated by a comma")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what.")