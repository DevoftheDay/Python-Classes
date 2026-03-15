actual_cost = float(input("Enter actual cost of items here"))
sale_amount = float(input("Please enter the sales amount"))

if(sale_amount > actual_cost):
    profit = sale_amount - actual_cost
    print("You made a profit of", profit)
else:
    print("No profit!")