units_consumed = int(input("Enter units consumed by yourself: "))

if units_consumed < 50:
    bill = (units_consumed*2.60)+25
elif  units_consumed <= 100:
    bill = (units_consumed*3.25)+35
elif units_consumed <=200:
    bill = (units_consumed*5.26)+45
else:
    bill = (units_consumed*8.45)+75

print(bill)
    
    