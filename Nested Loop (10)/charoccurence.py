string = input("Please enter your own word: ")

char = input("Please enter the character here: ")

i = 0
count = 0

while(i<len(string)):
    #brackets give index of the string
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("The number of", char, "'s", "in", string, "is", count)