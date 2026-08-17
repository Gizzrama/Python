def greet_customer():
    print("Hey there!")
    print("Welcome to our store!")

def calculate_price(price, items):
    return price * items

def calculate_change(total, pay):
    return pay - total

def thank_you(items):
    if items >= 5:
        print("Big sale! Thank you for shopping with us!")
    
    else:
        print("Thank you for shopping with Arts & Crafts Supplies!")

greet_customer()
price = float(input("What is the price for one art item?"))
items = int(input("How many items did you buy?"))

total = round(calculate_price(price, items))

print("The total is", total)



while True:
    pay = int(input("We only accept cash, how much will you pay?"))
    change = calculate_change(total, pay)

    if pay == total:
        print("No change required")
        break

    elif pay > total:
        print("The change is", change)
        break

    else:
        print("Please pay more")
        continue

thank_you(items)

print("\n")
print("---ART SUPPLIES FINAL BILL---")
print("\n")
print("Items bought ----------", items)
print("Price per item ----------", price)
print("Total Cost ----------", total)
print("Amount Paid ----------", pay)
print("Change Due ----------", change)
print("----End Bill----")

