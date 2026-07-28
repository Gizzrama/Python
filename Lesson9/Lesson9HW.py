print("HOLIDAY ACTIVITY PLANNER")

choice = int(input("\nWhere do you want to go during your holidays? Enter 1 for a Beach Holiday and enter 2 for a Mountain Holiday: "))

if choice == 1:
    print("Sure! Let's plan for a beach holiday.")
    print("We got two options: Swimming at the beach or building sandcastles.")
    choice = int(input("Enter 1 for swimming at the beach or enter 2 for building sandcastles: "))
    if choice == 1:
        print("\nHoliday planned. Let's swim at the beach!")
    
    elif choice == 2:
        print("\nHoliday planned. Let's build sandcastles at the beach!")
    
    else:
        print("\nPlease enter a valid number, either 1 or 2.")

elif choice == 2:
    print("Sure! Let's plan for a mountain holiday.")
    print("We got two options: Hiking, or camping at a campsite.")
    choice = int(input("Enter 1 if you want to hike, or enter 2 if you would like to go camping: "))
    if choice == 1:
        print("\nHoliday planned. Let's hike a mountain!")
    
    elif choice == 2:
        print("\nHoliday planned. Let's camp on a mountain!")
    
    else:
        print("\nPlease enter a valid number, either 1 or 2.")

else:
    print("Please enter 1 or 2")
