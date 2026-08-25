#***pyramid.py explains the basics of the for loop***

#In this particular piece of code, we are trying to create Floyd's triangle; a sequence of number starting from 1 and increasing by 1 each time in a pyramid pattern
#It is mainly used as a teaching tool for coders to learnn about loops and patterns.

n = int(input("Enter the number of rows: "))

#Instead of printing stars, we want ot print numbers increasing by 1 on each row.
#We make a variable called counter, and assign the value 0 to it.
counter = 0
for i in range(n):
    for j in range(0, i + 1):
       counter += 1
       print(counter, end= " ")
    print()

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(0, i + 1):
        print(i + 1, end = " ")
    
    print()
#Line 13 & 14: In line 13 we increment counter by one each time, so the number also gets increased by 1 each time it is printed on each row. 
#We print counter in line 14, since we want the numbers to be displayed, not stars this time. Everything else is the same.

#Line 19:
#The second for loop is basically Floyd's triangle, however t prints the same number i + 1 number of times on each row.
#Instead of printiong counter here, we print i + 1, so the i + 1 gets printed j (i + 1) number of times each row.
#This is easy once you go through the pyramid.py file.