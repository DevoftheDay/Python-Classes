from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("The date today is: ", today)
print("The Current time and date right now is: ", now)

print("\nDate Components: ", today.year, today.month, today.day)