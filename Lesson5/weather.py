#CONDITIONAL STATEMENTS
name = input("Enter your name:")
print(f"Hello, I am {name}, and I will be your travelling agent.")
temperature = int(input("What is the temperature?"))
is_raining = input("If it is raining, enter yes or no")
wind_speed = int(input("Enter the wind speed"))

#The if statement is used to print an output only if something is true or false
if temperature < 20:
    outfit = "jacket"
    print("It is a cold day, wear a ", outfit)
#else is the opposite of if; if something doesn't satisfy the if statement, the else statement is used to print the opposite
else:
    outfit = "T-shirt"
    print("It is a warm day, wear a ", outfit)

if is_raining == "yes":
    print("Bring an umbrella")

if wind_speed >= 30:
    print("It is a windy day")

else:
    print("It is a calm day")
print("Weather outfit peeker")
print("The temperature is ", temperature)
print("The wind speed is ", wind_speed)
print("Is it raining?", is_raining)


