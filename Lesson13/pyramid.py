#A nested for loop is exactly what it sounds like — a for loop written inside the body of another for loop. The key behavior to understand:
#The outer loop runs once per iteration, just like normal.
#But each time the outer loop takes a single step, the entire inner loop runs from start to finish before the outer loop is allowed to move to its next step.
#So if your outer loop runs 5 times, and your inner loop runs 3 times each time it's triggered, the inner loop's code actually executes 15 times total (5 × 3). 
#This is different from two separate loops one after another — here, the inner one is "nested" inside one single pass of the outer one.
#Nested for loops show up any time you're dealing with something that has two (or more) dimensions, or when for each item in a collection, 
#you need to do a full loop's worth of work. It is mainly used to print patterns and tables of any kind.

#We want ot print the character '*' as many times as the user wants it to be printed.
#Notice how we used to print only numbers before on for loops; characters and letters can also be printed.
#The code asks the user for the number of rows of '*' they want to print
n = int(input("How many rows of * do you want to print?"))

#This is the outer loop. It prints n, which is the variable that stores the deesired number of rows to be printed.
#Remember how the second parameter (the stop) of a for loop is always exclusive and the first parameter (the start) is always inclusive?
#Since the first row is labelled as 0, if we write n + 1, it will not print n since it starts from 0. The number of will go from 0 to n, which adds an extra 
#unwanted row because of the 0. Either we can start with (1, n + 1) or (0, n). If you don't understand, run the code and you will get it. 
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end = " ")
    print()

#Line 19: This is the inner loop, and it runs (n * i)/2 times, since that is the total number of stars. Run the code and plug this formula in if you want.
#j is just another type of variable just like i. You can technically use anything to represent the index in a for loop, however i and j are the most commonly used variables.
#Here, the second parameter is i + 1. As usual, the first parameter is 0. The j starts from 0, which basically prints 0 stars at first.
#The first row: In the first row, the value for i is 0, since that is the start parameter given for the outer for loop. For every i that is getting printed (basically the row),
#the j is also getting printed, but by i + 1 number of times. To simplify, in the first row i is equal to 0. Now starts from 0, and the number of stars in one row is i + 1. 
#So for the first row, j = i + 1, and i = 0. Thus j will be equal to 1, and hence the first row will have 1 star.
#This is the same with the second row when i = 1. j = i + 1, and so j = 2. So the second row will have 2 stars. The j is nothing but the number of stars in each row, and gets increased by 1 for each row number.
#Thi is how it creates a triangle pattern.

#Line 20: Th line 20 prints the character which is the star '*'. However the end keyword argument has been used here.
#The end keyword argument:
#        end is a named parameter (also called a keyword argument) that belongs specifically to the print() function. 
#        It's not a reserved word that Python understands everywhere — it only has special meaning when you use it inside print(...).
#        You could technically use end as a variable name elsewhere in your code.
#        That would never work with an actual keyword — you can't do for = 5 or if = 5, because those are reserved.
#        That would never work with an actual keyword — you can't do for = 5 or if = 5, because those are reserved.
#        What end does inside print():
#        By default, print() automatically adds a newline character (\n) after whatever it prints — that's why every print() call normally starts on a new line. 
#        The end parameter lets you override that default and choose what gets added instead of the newline.

#Here is the same code without the end keyword argument. This is to make you understand the functions and behaviours of end:
for i in range(0, n):
    for j in range(0, i + 1):
        print("*")
    print()

#        The end can also be used to assign a space between two characters. Notice how I wrote end = " "? The " " is what gives space between each star. 
#        I can also change the amount of space, just by altering the space inside "", just like this: "  " or "       "
#        You can try if you want

#Line 21: A blank print statement is added on line 21, inside the outer for loop but outside the inner for loop
#This is really about indentation and timing, so let's look closely at where it sits.
#It is inside the outer for i loop (so it runs once per row)
#It is outside the inner for j loop (so it does not run every time j changes — only after the inner loop is completely done)
#Why it needs to be there, specifically:
#Think about the sequence of events for one pass of the outer loop (say i = 2):
#   1) Outer loop starts row i = 2
#   2) Inner loop runs: prints 4 , 5 , 6  — all staying on the same line because of end = " " 
#   3) Inner loop finishes (no more j values left)
#   4) Now — and only now — print() runs, adding the newline
#   5) Outer loop moves to i = 3 and the whole thing repeats

#HERE'S IS THE SAME PIECE OF CODE WITHOUT THE BLANK print()
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end = " ")

#Ultimately, end = " " is the horizontal controller and helps keep the stars int eh smae line for each row, and the blank print statement is the vertical controller,
#and helps the horizontal piece of code to move onto the next row.

#HERE IS THE SAME PIECE OF CODE WITHOUT  end = " " AND THE BLANK print():

for i in range(0, n):
    for j in range(0, i + 1):
        print("*")

