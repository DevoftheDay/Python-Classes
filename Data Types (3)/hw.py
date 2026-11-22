memberName = input("Enter the member name here: ")
clubName = input("Enter your club's name here: ")
membernum = int(input("Enter your member number here: "))

print(type(memberName))
print(type(clubName))
print(type(membernum))


member = memberName[0:3:1]
print(member)

club = clubName[0:6:1]
print(club)

print(member, "is a member of the club that does", club)