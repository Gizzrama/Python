temp = int(input("Enter today's temperature in degrees Celsius: "))
rain = input("Is it raining? Please answer if yes or no: ").strip()
homeworkTime = int(input("Enter homework time in minutes: "))
freeTime = input("Have you got any freetime? Please answer if yes or no: ").strip()

if temp < 20:
    activity = "Play indoors"
    print(f"It is wise to {activity} because it is too cold.")

elif temp >= 20 and temp < 35:
    activity = "Play outdoors"
    print(f"It is nice and warm today, {activity}.")

elif temp >= 35:
    activity = "Play indoors"
    print("It is too hot, just play inside")

if rain == "yes":
    print("Reminder: It is recommended to not play outside because it is wet.")

if homeworkTime >= 90:
    needsBreak = "yes"
    print("You need a break every 90 minutes to avoid burnout.")

else:
    needsBreak = "no"
    print("You have a nice study time, you don't need a break.")

if freeTime == "yes":
    finalTask = "Hobby Time"
    print("Do whatever you want to do, such as spent time on your hobbies.")

elif freeTime == "no":
    finalTask = "Planning Time"
    print("Time for some better planning so you can have some freetime.")

else:
    print("Please enter a valid answer")

print("\n")
print("*****COMPLETE PLAN*****")
print("Temperature: ", temp)
print("Rain Status: ", rain)
print("Study Break Status: ", needsBreak)
print("Chosen Activity: ", activity)
print("Final Task: ", finalTask)


