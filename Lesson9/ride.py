#NESTED IF, ELIF AND ELSE STATEMENTS
print("We are from ride building company")
print("We provide bikes, cars and scooters.")
choice = int(input("Enter 1 for car, 2 for bike and 3 for scooter."))

if choice == 1:
    print("Bike chosen")
    print("We have three types of bikes:")
    print('1) Dirt Bike')
    print("2) Motorbike")
    print("3) Mountain Bike")
    choice = int(input("Enter 1 for Dirt bike, 2 for motorbike and 3 for mtb"))
   
   #This is an example of a nested if-statement. A nested statement is always inside another conditional statement or loop, and will only execute if the larger conditional statement or loop is true.
    if choice == 1:
        print("You have chosen dirt bike.")
        print("Top speed: 150 km/h")
        print("All terrain")
        print("Cost 2000 Rs/- for 1 hour")
    
    elif choice == 2:
        print("You have chosen motorbike bike.")
        print("Top speed: 240 km/h")
        print("Smooth on roads and dirt roads")
        print("Cost 3000 Rs/- for 1 hour")

    elif choice == 3:
        print("You have chosen MTB bike.")
        print("Top speed: 170 km/h")
        print("Versatile")
        print("Cost 3000 Rs/- for 1 hour")
    
    else:
        print("Enter a valid number")


elif choice == 2:

    print("Car chosen")
    print("We have three types of cars:")
    print('1) Compact Car')
    print("2) SUV")
    print("3) Jeep")
    choice = int(input("Enter 1 for compact car, 2 for SUV and 3 for Jeep"))
   
    if choice == 1:
        print("You have chosen compact car.")
        print("Top speed: 200 km/h")
        print("Smooth on roads and dirt roads")
        print("Cost 3000 Rs/- for 1 hour")
        
    #Nested elif
    elif choice == 2:
        print("You have chosen SUV.")
        print("Top speed: 240 km/h")
        print("Smooth on roads and dirt roads")
        print("Cost 4000 Rs/- for 1 hour")

    elif choice == 3:
        print("You have chosen Jeep.")
        print("Top speed: 220 km/h")
        print("Versatile")
        print("Cost 4000 Rs/- for 1 hour")

elif choice == 3:
    print("Scooter chosen")
    print("For 1 hour, it will cost 2000 Rs/-")
    hours = int(input("For how many hours do you want to use our scooter"))
  
    total_cost = hours * 2000
    gear_kit = int(input("Do you want a gearkit? Enter 1 for yes and 2 for no."))
   
    if gear_kit == 1:
        print("It will cost an additional 2000 Rs/- for modifications for seats and handles")
        new_total_cost = total_cost + 2000
    
    else:
        print("No modifications required")
    
    print(f"The total price for {hours} hours is {total_cost}. The total price for additional modification for {hours} hours is {new_total_cost}")



else:
    print("Please enter a valid number from 1 - 3.")

