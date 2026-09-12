#In this piece of code, we are trying to cube any number. 
#We define cube, and we enter number as an argument since it is fundamental in this fnction
def cube(number):
    n = number * number * number 
    return n

#Line 4: We assign a variable n, so that it can store the cube of the number (number multiplied by itself thrice)
#Line 5: We return n so it can be used outside the function block.
#The line below represents the chronological sequence of the code, which starts from under the line.
#---------------------------------------
#Line 12: User input for them to enter any number
number = int(input("Enter any number"))
#Line 14: Uses user-defined function 'cube' to cube user's number. Stored in a variable so it can be used later.
a = cube(number)
#Line 16: Prints cube of number.
print(f"The cube of {number} is {a}.")






