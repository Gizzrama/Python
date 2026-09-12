#In this piece of code, we are trying to find the factorial of any number.
#A factorial is the result of multiplying a positive whole number by every whole number that comes before it down to one. It is represented by an excalmation mark '!'
#It does not work for non-whole numbers and negative numbers; only counting numbers.
#E.g. 4! = 4 * 3 * 2 * 1 = 24
def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1) 

#Line 5: We define a new function called factorial and pass the argument number since it is useful for this 
#Line 6 - 7: We provide an if conditional statement, stating that if number is equal to 0 or 1, then the factorial should be 1 since 0! & 1! is equal to 1.
#We return 1 so that it can be used outside the def block
#Line 8: Since a factorial is the multiplication of the number and all the number before it until 1, we have to decrement number by 1 so the number actually get subtracted by 1.
#Ironically, we are defining the function, yet we are using the function to define itself. This is called recursion.
#Recursion is when something 'recurs' or repeats. A factorial is a repetition of n - 1. 
#The form a factorial is n! = n * (n - 1)!. Notice the '!' after (n - 1). This indicates the factorial of the number 1 less than n. Thus we use recursion here
#to repeat the multiplitcation of factorials from 1 to n. We then return it so the number sentence can be used outside the def block.
#Example: number = 4
#number != 0 nor number != 1.
#∴ number! != 1
#Next Step: 4 * (4 - 1)!
# = 4 * 3
# = 12 * (3 - 1)!
# = 12 * 2
# = 24
# = 24 * (2 - 1)!
# = 24 * 1
# = 24
#∴ 4! = 24
#This is how an actual factorial works, and how it works in code as well. The exclamation mark is just like a function: it represents something, here the mathematical conept of factorials.
#--------------------------------------
#Line 35: Integer user input to get a number
#Line 36: Calling the function factorial inside a variable
#Line 37: Printing the vairable
    number = int(input("Enter any number"))
    a = factorial(number)
    print(f"The factorial of the number {number} is {a}.")
