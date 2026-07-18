#Step 1
name = input("Please enter your full name:")
club = input("Which club are you part of?")
#Step 2
memberNumber = 155.990392
print(memberNumber)
pointsEarned = int(input("Please enter the number of points you have earned:"))
eventCount = int(input("How many events have you completed?"))
meetingHours = int(input("For how many hours have you attended our events?"))
activeStatus = bool(input("If you are an active member, please type type true. If not, then type false:"))
#Step 3
print(f"The type for member number is {type(memberNumber)}")
print(f"The type for how many points you earned is {type(pointsEarned)}")
print(f"The type for your event count is {type(eventCount)}")
print(f"The type for your meeting hours is {type(meetingHours)}")
print(f"The type for your status is {type(activeStatus)}")
#Step 4
m = str(memberNumber)
p = str(pointsEarned)
e = str(eventCount)
a = str(activeStatus)
print(m,"|", p, "|", e, "|", a,)
#Step 5
firstThree = name[0:3]
last = name[-1]
badgeCode = firstThree + last
print(firstThree)
print(last)
print(badgeCode)
#Step 6
secretCode = club[::-1]
print("Secret Club Code: ", secretCode)
#Step 7
badgeLine1 = "Club Member: " + name
badgeLine2 = "Identification: " + m 
badgeLine3 = "Points: " + p + e + a
badgeLine4 = "Club Code: " + secretCode
print("School Member Badge")
print(f"\n{badgeLine1}, \n{badgeLine2}, \n{badgeLine3}, \n{badgeLine4}")

