print("Enter marks obtained in each class here: ")
math = float(input("Input math marks here: "))
english = float(input("Input english marks here: "))
science = float(input("Input science marks here: "))
history = float(input("Input history marks here: "))

sum = math + english + science + history
print("sum of your marks is: ", sum)

totalpercent = (sum/400)*100

print(totalpercent)