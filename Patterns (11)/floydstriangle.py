print("Half Pyramid Pattern of Stars(#):")

n = int(input("Enter the number of rows: "))

count = 0

for i in range(n):

    for j in range(i+1):
        count = count+1
        print(count, end=" ")
    print()