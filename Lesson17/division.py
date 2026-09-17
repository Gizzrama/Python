try:
    numerator, denominator = eval(input("Enter the numerator and the denominator, separated by a comma"))
    print("The value is", numerator/denominator)

except ValueError as e:
    print("This is a value error", e)

except ZeroDivisionError as e:
    print("This is an exception; a zero division error", e)

except SyntaxError as e:
    print("There should be a comma, this is a SyntaxError", e)

except:
    print("This is an exception")

finally:
    print("This is division")

#*FOR INFO ON WHAT THE try AND except BLOCKS ARE, CHECK even.py*
#Line(s) 5, 8, 11: The except block is used to avoid errors from occurring since errors stop the flow of a piece of code. We use the except block in almost all scenarios.
#For example when there is a user input wherein the user has to enter a certain answer, we might use except block to enter an alternative to the error code/number since 
#users might enter something that trigger the code to throw an error.

#Some common errors:
#(1) ValueError:
#--> Raised when a function gets an argument of the right type but an inappropriate value.
#--> int("hello") - ValueError: invalid literal for int() with base 10: 'hello'

#(2) ZeroDivisionError:
#--> Raised when you try to divide (or modulo) a number by zero.
#--> 10 / 0 - ZeroDivisionError: division by zero

#(3) TypeError:
#--> Raised when an operation is applied to an object of an inappropriate type.
#--> "5" + 5 - TypeError: can only concatenate str (not "int") to str

#(4)SyntaxError
#--> Raised when Python's parser can't understand your code because it violates the language's grammar rules — this happens before the code even runs.
#--> if True
#       print("hi")  # SyntaxError: expected ':'

#The e:
#Notice how I wrote 'excepts ValueError as e:'
#The e is a variable that stores the explanation of the error, somewhat like the i or j in for loops, where it is the index of the code inside it.

#The finally:
#The finally prints a statement regardless of whether there are errors or not. The finally requires a try block if you must add it, however not the except block,
#since it carries out a piece of code and runs it regardless of whether there are errors or not.

#Line 2:
#The eval is used to enable two or more types of datatypes.
#A built-in Python function that takes a string (or compiled code object / bytes) and executes it as a Python expression, returning the result.
#How it works:
#   Parses the input as if you'd typed it directly, then runs it and returns the value.
#   Example: eval("2 + 3") → 5
#   Can use existing variables: eval("y * 2") where y is already defined.

#What it can evaluate:
#   Only expressions — things that produce a value (2+3, [1,2,3], len('hi')).
#   Cannot run statements like if, for, while, or assignments (x = 5) — that's what exec() is for.

#Notice how I wrote 'separated by a comma' in Line 2?
#You must enter a comma only when:
#You want the user to enter multiple values at once (like a tuple: 1, 2, 3)
#You're building a list or calling a function with multiple arguments (max(1, 2, 3))