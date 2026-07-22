counter = 0
dayCounter = int(input("Enter the desired number of times u want to run the code"))

#The 'while' statement is an infinite loop, and keeps repeating whatever input is given
while True:
    counter = counter + 1 #incrementation is increasing a value by 1. In programming, this can be done by assigning an integer to a vraiable, and adding 1 to the variable as shown on this line

    if counter > dayCounter:
        break #break is a keyword in python which stops a loop

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
    



    

    



