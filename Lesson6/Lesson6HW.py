print("LIBRARY VISIT PLANNER")
print("\n")
print("Please answer the three upcoming questions to proceed")
print("\n")
day = input("What day is it today?").strip().capitalize()
weather = input("What is weather like today?").strip().capitalize()
bookReturn = input("Do you need to return a book? Please answer if yes or no: ").strip().capitalize()
print(f"{day} | {weather} | {bookReturn}")

print("\n")
if day in("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("It is a regular school day")

elif day in("Saturday", "Sunday"):
    print("Today is a weekend! Relax for today.")

else:
    print("Please enter a valid day")

if weather == "sunny" and bookReturn == "yes":
    print("Lovely day! Return your book and borrow a new one.")

if weather == "rainy" or weather == "cloudy":
    print("Looks overcast eh? Carry an umbrella.")

if not bookReturn == "yes":
    print("There is no book to return. Have a nice day!")

if weather == "sunny" and bookReturn == "yes" or day in("Saturday", "Sunday") and not bookReturn == "no":
    print("Today is a brilliant day to visit the library! Have a quiet and peaceful time at the library.")