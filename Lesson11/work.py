
while True:
    print("There are five tasks to do: if you enter 1 task1 will be done and if you enter 2 task2 will be done. 3 for task3, 4 for task4 and 5 for task5.")
    choice = int(input("Enter 1 for task1, 2 for task2, 3 for task3, 4 for task4, 5 for task5. Enter 100 if you want to exit."))
    
    if choice == 100:
        print("You have ended the loop")
        break

    if choice == 1:
        print("You can play volleyball")
    
    elif choice == 2:
        print("You can play cricket")
    
    elif choice == 3:
        print("You can sleep")
    
    elif choice == 4:
        print("You can study")
    
    elif choice == 5:
        print("You can play some games.")
    
    else: 
        print("You have entered an invalid number")
    
