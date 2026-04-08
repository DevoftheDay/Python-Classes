def total_calc(bill_amount, tip_perc): #defining function
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2) #rounding to 2 digits
    print(f"Please pay ${total}")

total_calc(150, 20) #150$ bill with 20 percent tip
