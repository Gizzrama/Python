#NESTED LOOPS
#Nested loops are used when you want to repeat a piece of code several times. Here, we are asking the customer to draw money from the atm. 
#The outer while loop ensures that the atm works regardless of any customers, and the inner while loop runs code for every customer who approaches the atm.

#Line 6 basically works forever. The loop doesn't break since it represents the working ATM.
while True:
    name = input("Please enter your name").strip() #Lines 7 & 8 are basically asking for the user's name and withdrawal amount
    atm = int(input("How much do you want to withdraw? "))

    if atm < 0:
        print("Please withdraw more than 0 rupees.")
        continue #This keyword is used in python when you want to skip a line. This is the inverse of break, and can only be used in loops.
        #Let's say the user has entered 0 or less than 0 as their withdrawal amount. It prints the statement, and what the coninue does is that it skips the response and asks the question again. Here the question is inside the variable 'atm'  

    #Now we're onto the money part, where ATM prints the notes 
    #The logic behin lines 18 - 25 is to give cash in the most effective way possible i.e, using the least amount of notes to reach the user's desired amount of money.
    #Hypothetically, here the ATM can only print 10, 50, 100 and 500 rupee notes
    #Now a variable is set for each note. What the floor division does is that it basically tells us the maximum number of times a note can be produced according the user's desired amount of cash.
    #E.g. User wants 6660 in cash. The user would want to start with 500 rupee notes, since they hold the highest value, and because they can reduce the number of notes
    #     The floor division will basically print 13 500 rupee notes
    #     Then it will move on to 100 rupee notes, and it will print 1
    #     Then the 50 rupees, which is just 1
    #     And finally the 10 rupee notes, which is also 1 
    while True:
        notes500 = atm//500
        atm = atm%500
        notes100 = atm//100
        atm = atm%100
        notes50 = atm//50
        atm = atm%50
        notes10 = atm//10
        remaining = atm%10

        #These lines are giving a choice to the user, to check if they really want he number of notes the ATM gives or the number they want.  
        #Here, they don't have to start with 500 rupee notes, rather they can just go for 100 rupee notes. So if they want onyl 100 rupee notes and no 500 rupee notes and they asked for 6000 rupees, the ATM will provide 60 100 rupee notes
        #Pressing 100 will basically end the loop, when the user has acquired all the cash they want
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
        
        
            