base = int(input("Enter a base number for an exponent here: "))
exp = int(input("Enter an exponent number: "))
num = 1


for i in range (exp):
  num = num * base

print(num)

