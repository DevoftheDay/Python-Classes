amount = int(input("Please Enter Amount For Withdrawal : "))

note_100 = amount//100
note_50 = (amount%100)//50
note_20 = ((amount%100)%50)//20
note_10 = (((amount%100)%50)%20)//10
note_5 = ((((amount%100)%50)%20)%10)//5
note_1 = (((((amount%100)%50)%20)%10)%5)//1

print("note of $100", note_100)
print("note of $50", note_50)
print("note of $20", note_20)
print("note of $10", note_10)
print("note of $5", note_5)
print("note of $1", note_1)
