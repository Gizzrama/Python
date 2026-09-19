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

#eval() function
#eval() is a built-in python function that takes a string containing a Python expression
#First let's understand what an expression is.
#A Python expression is a piece of code that produces a value. If you can put it on the right side of an = sign or pass it into print(), it's an expression.
#Types of expressions:

#    | Expression |      | Type of expression |      | Result |
#|---------------------|-------------------------|---------------|
#| `5`                 | Literal value           | `5`           |
#| `x + 3`             | Arithmetic              | `15`          |
#| `"hi" + " there"`   | String concatenation    | `"hi there"`  |
#| `len("hello")`      | Function call           | `5`           |
#| `[1, 2, 3][0]`      | Indexing a list         | `1`           |
#| `x > 10`            | Comparison              | `True`        |
#| `10, 2`             | Tuple                   | `(10, 2)`     |
#| `n * 2 if n else 0` | Conditional expression  | `8`           |

#An expression is not the same as a statement. 
#A statement is an instruction that does something but doesn't produce a value.
#Examples:
#   x = 5                # assignment statement
#   import os            # import statement
#   if x > 3:            # if statement
#       print("big")        
#   for i in range(3):   # loop statement

#You can't write y = (x = 5) or print(import os). An expression is anything that can be wrapped inside a print()
#print(x = 5) #Error --> Statement
#print(3 + 6) #9 --> Expression
#Why is x = 5 not an expression when it says you can put it on the right side of an (=) sign?
#Because it doesn't produce any value, just assigning x to 5.

#Back to eval()

#What it does
#   Parses the string as a Python expression
#   Evaluates it and returns the result
#   The returned value can be any type (int, str, list, tuple, etc.)
#   Handles expressions only, not statements like x = 5 or import os#   
#   Can access variables in the current scope unless globals/locals are supplied

#When it is used
#   Quick experiments or testing in the interpreter
#   Evaluating simple maths typed as text, e.g. eval("3 + 4")
#   Reading multiple values from one line of input, e.g. a, b = eval(input())
#   Building small calculators or tools where the input is fully trusted
#   ynamically running expressions stored as strings

#When to avoid it
#   With untrusted input (user input, files, network data), since it runs any Python code in the string
#   In real applications, where safer options exist: ast.literal_eval(), json.loads(), or explicit parsing with int()/float() and .split()

#We used it in this user input since the usre is entereing two values, and with a normal integer user input, it doesn't take two or more values.
#eval() takes a string (here it converts numerator, denominator into a string) that contains a Python expression
#numerator, denominator = tuple = expression
#So it becomes (numerator, denominator)
#Then the end resuld is numerator/denominator
