#FUNCTIONS: Functions are words in python that have certain behaviours. For instance, the print() is a function which prints the output in the terminal. 
#len() is also a function which checks the number of characters in a set. These functions have certain behaviours that are pre-defined by developers who created python.
#However, a programmer can also create their own function that isn't a built-in function. 
#We use the def keyword when we want to define a function. The def is always followed by the new function, and a pair of brackets. Every function in python is followed by a pair of brackets.

#Here we want to define the function greet_customer()
#Lines 9 & 10 are what gives the functions its behaviours. Here, if you call the function, it will print these two messages.
def greet_customer():
    print("Hello, welcome to our lemon juice stall!")
    print("Fresh lemonade just for you")

#Now just like built-in functions, anything can go inside the brackets of a user-defined function.
#When variables or other keywords are related to our new function, we must pass them inside the brackets. These are called arguments in python.
#Here price and cups are variables that have certain values. The calculate() function is used to calculate the total price. So we multiple price by cups inside the function.
def calculate(price, cups):
    return price * cups

def calculate_change(a, pay):
    remaining = a - pay
    return remaining

def thanks(cups):
    if cups >= 5:
        print("That's a big order. Thank you so much for your support!")
    
    else:
        print("Thank You")


greet_customer() # --> This is how you call a function, so its code can run
price = float(input("What is the price per cup?"))
cups = int(input("How many cups do you want?"))
a = calculate(price, cups)
print("The total price of the cups are", a)

pay = float(input("How much will you pay"))
b = calculate_change(a, pay) # --> You can also store the value of the function inside a variable so that it can be reused throughout the code. Also note that arguments must be written if you are calling a function with arguments, like this one.
print("The remaining amount is", b)

thanks(cups) # --> Function called with its parameters. If you do not call a function with its parameters if it does have parameters, then the code will not execute.
print("\n")
print("\n")
#The return keyword:
#The return keyword is used to return a value back out of a function, so that the value can be stored in a variable and reused anywhere. 
#Now the return keyword is different from print()

#Imagine you ask a friend: "hey, what's 3 + 5?"
#If your friend says it out loud ("it's 8!") but doesn't write it down — that's like print(). You heard the answer, but you don't actually have it. You can't do anything with it afterward.
#If your friend writes it on a sticky note and hands it to you — that's like return. Now you physically hold "8" in your hand. You can pocket it, add it to another number, hand it to someone else — whatever you want.
#Example
print("The return keyword:")
#Without return
def add(a, b):
    print(a + b)       #friend says it out loud

x = add(3, 5)          #you get nothing to hold onto
print(x)               #None

#With return
def add(a, b):
    return a + b       #friend writes it on a sticky note and hands it over

x = add(3, 5)          #now you're holding "8"
print(x)               #8

# print() vs return
# -------------------------------------------------------------------------------
# |                    | print()                          | return                          |
# -------------------------------------------------------------------------------
# | What it does       | Displays a value on screen       | Hands a value back to the caller |
# | Is the value saved?| No - gone after displaying       | Yes - if assigned to a variable  |
# | Can you reuse it?  | No                               | Yes                              |
# | Effect on function | Doesn't stop the function        | Immediately ends the function    |
# | Independent?       | A function can print, return, both, or neither - they don't affect each other
# -------------------------------------------------------------------------------

#What return does:
#  --> Sends a value back from a function to whoever called it.
#  --> Immediately ends the function — any code after return inside that function does not run.
#  --> If a function has no return (or a bare return), it automatically gives back None.

#Why it should be used:
#   Without return, a function can still do things (print, modify something, etc.), but it can't hand a usable result back to your code. 
#   Return is what makes a value capturable — usable elsewhere in your program.

#Why you must store the returned value in a variable:
#  --> Reuse it multiple times without recomputing
#  --> Combine it with other values
#  --> Use it later or conditionally (if, else, try etc.)

#Return vs Variable
#Return makes the function's result available to be used outside the function (once, immediately, or captured for later).
#Storing that value in a variable is what lets you hold onto it and reuse it repeatedly, instead of it being used once and discarded.
#The moment you need to reuse, combine, or hold onto a value, you need a variable — and that only works if the function actually returns something.

#What happens if you don't store it:
#The returned value is computed, but then discarded — nothing keeps hold of it.
 
#What happens if you don't use return:
#  --> The function still runs all its code (prints, modifies things, etc.).
#  --> But calling it and assigning the result to a variable gives you None.
#  --> You lose the ability to use the function's result anywhere else in your program — no combining it with other values, no reusing it, no passing it along.

#Ths is the importance of the return keyword in python. The return keyword is only used when defining a function in python.