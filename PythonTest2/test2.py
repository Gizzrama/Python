#Prompt: Build a calculator that uses a separate function for each operation.
#The user picks an operation and enters two numbers.
#Your program handles invalid input and division by zero without crashing.


def addition(a, b):
   return a + b


def subtract(a, b):
   if a > b:
       return a - b


   elif b > a:
       return b - a


   else:
       return 0


def multiply(a, b):
   return a * b


def divide(a, b):
   return a / b


while True:
   try:
       a = float(input("Enter value for a: "))
       b = float(input('Enter value for b: '))




       choice = int(input("Enter 1 to add, 2 to subtract, 3 to multiply and 4 to divide and 5 to exit: "))


       if choice == 1:
           print(f"The sum of {a} and {b} is {addition(a, b)}")


       elif choice == 2:
           print(f"The difference of {a} and {b} is {subtract(a, b)}")


       elif choice == 3:
           print(f"The product of {a} and {b} is {multiply(a, b)}")


       elif choice == 4:
           print(f"The quotient of {a} and {b} is {addition(a, b)}")


       elif choice == 5:
           print("End loop")
           break


       else:
           print("Enter numbers 1 - 4")




   except ValueError:
       print("Values a & b must be float values, and choice must be an integer.")


   except ZeroDivisionError:
       print("One of the numbers can't be zero.")


   except:
       print("there is an exception")





