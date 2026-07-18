#Step 1
print("TEAM")
blue = 1068
red = 2096
green = 989
yellow = 2545
orange = 1789

#Step 2
total = blue + red + green + yellow + orange
average = total/5
print("Total Points Accumulated: ", total)
print("Points per team on average: ", average)

#Step 3
starsPerPoint = 5
totalStars = total*5
print("Total Number of Stars: ", starsPerPoint)

#Step 4
fullBoxes = totalStars//25
leftover = totalStars%25
print("Full boxes of stars: ", fullBoxes)
print("How many stars are leftover: ", leftover)

#Step 5
lastWeek = 9384

print("Was last week's total better than this week's? ", total < lastWeek)
print("Was last week's total equal to this weeks's total? ", total == lastWeek)
print("was last week's total less than this week's total? ", total > lastWeek)

#Step 6
total += 2050
print("Bonus points for good behaviour: ", total )
total -= 1098
print("Missed points because of incomplete tasks: ", total)


