while True:
    name = input("Please enter your name").strip()
    atm = int(input("How much do you want to withdraw? "))

    if atm < 0:
        print("Please withdraw more than 0 rupees.")
        continue

    while True:
        notes500 = atm//500
        atm = atm%500
        notes100 = atm//100
        atm = atm%100
        notes50 = atm//50
        atm = atm%50
        notes10 = atm//10
        remaining = atm%10

        choice = int(input("Enter 1 for amount of 100 rupee notes, 2 for 500 rupee notes, 3 for 50 rupee notes and 4 for 10 rupee notes. Enter 100 to break the loop"))
        if choice == 100:
            break
        if choice == 1:
             print("The notes of 100 are: ", notes100)
        
        elif choice == 2:
             print("The notes of 500 are: ", notes500)

        elif choice == 3:
             print("The notes of 50 are: ", notes50)
        
        elif choice == 4:
             print("The notes of 10 are: ", notes10)
        
        else:
            print("Invalid choice")
        
        
            