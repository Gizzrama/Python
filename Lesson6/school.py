print("SMART SCHOOL DAY PLANNER")
print("Answer three questions")
day = input("enter any day from Monday to Saturday: ").strip().capitalize()
homework = input("for how many subjects did u get homework on any of these days?").strip().lower()
weather = input("What is the wetaher like?").strip().lower()
print(day, homework, weather)

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

if weather == "sunny" and homework == "yes":
    print("It's good to go out")

if weather == "rainy" or weather == "cloudy":
    print("Take your umbrella")

if not homework == "yes":
    print("Homework not done yet")

#Combination
if weather == "rainy" and not homework == "yes":
    print("Best plan: Do homwork")

elif weather == "sunny" and homework == "yes" and not day in ("Monday", "Tuesday", "Thursday"):
    print("Best plan is to go outside")

else:
    print("Do your homework")







