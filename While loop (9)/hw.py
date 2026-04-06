num = int(input("Enter a number here: "))

counter = 0
temp = num
while num > 0:
    digit = temp % 10
    counter += digit + 1
    temp //= 10

print(num)