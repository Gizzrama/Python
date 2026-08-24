import random

while True:
    action = random.randint(1, 3)
    a = int(input("enter 1 for rock, 2 for paper and 3 for scissors"))

    if a == action:
        print("It is a tie.")

    elif a == 1:
        if action == 2:
            print("Paper covers rock. Computer Wins!")
        
        else:
            print("Rock hits scissor, user won!")
    
    elif a == 2:
        if action == 1:
            print("Paper cover rock. User wins!")
        
        else:
            print("Scissor cuts paper. Computer wins")
    
    elif a == 3:
        if action == 1:
            print("Rock hits scissor. Computer Wins!")
        
        else:
            print("Scissors cut paper. User Wins!")

    else:
        print("Invalid input. Enter number between 1 and 3")


