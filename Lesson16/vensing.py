def calculate_change(total, price):
    return total - price

while True:
    print("You can only enter coins of 1, 2, 5, and 25")
    print("We have chips, cool drinks, milkshakes and fruit juice. \nChips cost 50 Rs, cool drinks cost 30 Rs, milkshakes cost 40 Rs and fruit juice cost 60 Rs")
    coin1 = int(input("How many coins of 1 rupees do you want?"))
    coin2 = int(input("How many coins of 2 rupees do you want?"))
    coin5 = int(input("How many coins of 5 rupees do you want?"))
    coin25 = int(input("How many coins of 25 rupees do you want?"))

    total = coin1 + coin2 * 2 + coin5 * 5 + coin25 * 25
    print("This is the total amount which you have:", total)

    choice = int(input("Enter 1 for chips, 2 for cool drinks, 3 for milkshakes and 4 for fruit juice. Press 5 to exit."))

    if choice == 1:
        print("You have chosen chips and it will cost you 50 Rs")
        a = calculate_change(total, 50)
        print("The remaining value is", a)
    
    elif choice == 2:
        print("You have chosen cool drinks and it will cost you 30 Rs")
        a = calculate_change(total, 30)
        print("The remaining value is", a)
    
    elif choice == 3:
        print("You have chosen milkshake and it will cost you 40 Rs")
        a = calculate_change(total, 40)
        print("The remaining value is", a)
    
    elif choice == 4:
        print("You have chosen fruit juice and it will cost you 60 Rs")
        a = calculate_change(total, 60)
        print("The remaining value is", a)
    
    else:
        print("Exiting...")
        break
    
    

      
    

    