import math
print("---GROCERY BILLING PROGRAM---")
low_price = 0
medium_price = 0
high_price = 0
customer_served = 0
total_sales = 0
name = input("What is your full name? ").strip().capitalize()
items = int(input("Please enter the number of grocery items your are buying: "))

while True:
    print(name)
    print(f"Hi {name}, start billing")

    if items == 0:
        print("Error: Please enter a number greater than 0")
        continue

    print(f"Billing for customer {name}")
    item_number = 1
    customer_bill = 0
    
    while item_number <= items:
        item_name = input("What is the item you are buying? Enter the company name and the full name on the sticker: ")
        quantity = int(input("How much of these items are you buying? "))
        price = float(input("What is the price of a single unit of your item (e.g. one tomato)?"))

        item_price = quantity * price
        customer_bill += item_price
    
        if item_price <= 10:
            print("Nice price")
            low_price += 1
    
        elif item_price > 10 and item_price <= 70:
            print("Medium priced")
            medium_price += 1

        else:
            print("Expensive")
            high_price += 1

            item_number += 1

        end = int(input("Enter 100 to end billing, and 0 to continue: "))

        if end == 100:
            break
        
        elif end == 0:
            continue
        
        else:
            print("Error: Enter either 100 or 0 to proceed.")

    customer_served += 1
    total_sales += customer_bill

    print("Billing Complete! Have a nice day.")

    repeat = input("Next customer please. Yes or no: ")
    if repeat != "yes":
        break

print("")
print("GROCERY REPORT")
print("")

for i in range(1, 4):
    if i == 1:
        print("Low priced items: ", low_price)
    
    elif i == 2:
        print("Medium priced items: ", medium_price)
    
    else:
        print("Expensive items: ", high_price)

print(f"Total Price: ${total_sales}")
print(f"Customers Today: {customer_served}")
print("\nBilling Closed")

    




    
