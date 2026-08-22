#PROMPT: You will create a helper program for a parking ticket payment machine. The program will keep accepting coins until the ticket price is
#reached. It will reject invalid coins, skip that turn with continue, stop the loop with break once enough money is inserted, calculate the 
#change using a function that returns a value, and use pass when no change needs to be printed.
def change(price, total):
    return total - price

price = 50
print("Parking Ticket Payment")
print("\n")
amount = 0

while True:
    print("Welcome!")
    print("\n")
    print(f"The parking price is ₹{price}. We only accept coins")
    total = int(input("How much will you pay?"))

    if total < price:
        print("Not enough money")
        print("\n")
        continue

    else:
        pass
    while True:
        print("\n")
        coins = int(input("Enter 1 to insert a ₹1 coin, 2 for ₹2, 5 for ₹5, 10 for ₹10 and 20 for ₹20. Enter 100 to exit after total amount is paid."))
        amount = amount + coins

        if coins == 1 or coins == 2 or coins == 5 or coins == 10 or coins == 20:
            pass
        
        elif coins == 100:
            break
        
        else:
            print("We only accept cash, please try again")
            print("\n")
            continue

        if amount >= total:
            print("You have paid.")
            break
        
        else:
            continue
        
    if total > price:
        print("The change due is", change(price, total))
        
    elif total == price:
        print("No change")
        
    else:
        pass

    print("\n")
    print("----------")
    print("RECEIPT")
    print("----------")
    print("Price:", price)
    print("Total amount paid:", total)
    print("Change:", change(price, total))
    print("-----------")
    print("\n")
    print("Thanks! Have a nice day 😊")
    print("\n")
    print("\n")
    continue
    

    

    



        
    