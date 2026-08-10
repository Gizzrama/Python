
def greet_customer():
    print("Hello, welcome to our lemon juice stall!")
    print("Fresh lemonade just for you")

def calculate(price, cups):
    return price * cups

def calculate_change(a, pay):
    remaining = a - pay
    return remaining

def thanks(cups):
    if cups >= 5:
        print("That's a big order. Thank you so much for your support!")
    
    else:
        print("Thank You")


greet_customer()
price = float(input("What is the price per cup?"))
cups = int(input("How many cups do you want?"))
a = calculate(price, cups)
print("The total price of the cups are", a)

pay = float(input("How much will you pay"))
b = calculate_change(a, pay)
print("The remaining amount is", b)

thanks(cups)








