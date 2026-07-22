print("SMART SCHOOL DAY PLANNER")
print("Answer three questions")
day = input("Enter any day from Monday to Saturday: ").strip().capitalize() 
homework = input("You got homework?").strip().lower()
weather = input("What is the weather like?").strip().lower()
print(day, homework, weather)

#.strip(), .capitalize(), .lower() and .upper() are functions in python that are used to tweak some errors
#The strip functions ignores all spaces the user gives during a user input. 
#The capitalize function ignores the first capitalised letter in a string
#The lower and upper functions convert all letters to lowercase or uppercase respectively
#The in operator is a shortcut, rather than using or. It has the same behaviour as an or operator
if day in ("Saturday", "Sunday"):
    print("Weekend: enjoy your freetime!")

elif day == "Monday":
    print("First day of the week")

elif day == "Friday":
    print("Last day of school")

elif day in ("Wednesday", "Tuesday", "Thursday"):
    print("Normal school day")

else:
    print("Enter a valid day")

#The and operator combines two conditions and runs only if both of the conditions are true
if weather == "sunny" and homework == "yes":
    print("It's good to go out")

#The or operator works if at least one of the conditions are true
if weather == "rainy" or weather == "cloudy":
    print("Take your umbrella")

#The not operator switches True to False, and false to true.
if not homework == "yes":
    print("Homework not done yet")

#COMBINING TWO OR MORE OPERATORS
if weather == "rainy" and not homework == "yes":
    print("Best plan: Do homework")

elif weather == "sunny" and homework == "yes" and not day in ("Monday", "Tuesday", "Thursday"):
    print("Best plan is to go outside")

else:
    print("Do your homework")







