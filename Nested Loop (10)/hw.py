low_price = 0
medium_price = 0
high_price = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    input("What is your name: ")
    item_count = int(input("How many items are you buying: "))
    if item_count<=0:
        print("You have no items.")
        break
    customer_total = 0
    item_number = 0

    while item_number < item_count:
        item_count -= 1
        item_name = input("Item name: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))

        if price <= 0:
            print("The item is free.")
        if quantity <= 0:
            print("You don't have any of this item.")

        item_total = price * quantity
        print(f"item_name: {quantity} x {price} = {item_total}")
        customer_total += item_total
        if price < 50:
            low_price += quantity
        elif price >= 50:
            medium_price += quantity
        else:
            high_price += quantity

    customer_total += 1
    total_sales += customer_total

    print(customer_total)
    ans = input("Next customer? (Y/N): ")
    if ans == "N":
        billing = False







        