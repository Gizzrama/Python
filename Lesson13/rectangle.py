#***pyramid.py explains the basics***

#This is basically printing a pyramid, but we don't add i + 1, and we ask for the number of columns and the rows. 
#This is easy, once you understand how to create a pyramid.
n = int(input("How many rows of * do you want to print?"))
c = int(input("How many columns of * do you want to print?"))

for i in range(n):
    for j in range(c):
        print("*", end = " ")
    print()