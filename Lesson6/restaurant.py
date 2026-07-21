counter = 0
dayCounter = int(input("Enter the desired number of times u want to run the code"))

while True:
    counter = counter + 1

    if counter > dayCounter:
        break

    day = input("Enter the day: ")

    if day in ("Saturday", "Sunday"):
        print("We only serve dosa")

    elif day == "Monday":
        print("We serve uttapam")

    elif day == "Tuesday":
        print("We serve idlis on Tuesday")

    elif day in ("Wednesday", "Thursday", "Friday"):
        print("We sevre pulao on these days")

    else: 
        print("Enter a valid day")
    



    

    



