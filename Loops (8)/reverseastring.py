string = input("Enter a word here: ")

string2 = ("")

for i in string:
    string2 = i + string2

print("This is the original string: ", string)
print("This is the reversed string: ", string2)