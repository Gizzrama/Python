#This is exception handling
#An exception is an unusual condition that interrupts a program's normal flow, stopping the rest of the code from running. 
#It's different from a syntax error, which happens before the program even starts, because an exception occurs while the program is actually running.
#Essentially exception handling is preventing errors from occurring in a piece of code.

#The try and except keywords are conditional statements, that run code based on if the condition is True or false.
#The try keyword handles risky code, which might result in an error. You write whatever code you want to write inside the try block, and the try block holds the risky code.
#Just like if-else statements, except needs try, but try doesn't need except. The try block can run without except. This is because the try block is like checking 
#the risky code for any errors, and the except block needs this to sabotage any errors. But the try block doesn't need the except block, since it just stores risky
#code, and doesn't deal with errors itself, like the except block.
valid = False
while not valid:
    try:
        number = int(input("Enter a number"))
        print("The number is", number)
        valid = True

        if number % 2 == 0:
            print("It is an even number")
        
        else:
            print("it is an odd number")

    except ValueError as e:
        print("Invalid number", e)
    
    except:
        print("This is an exception")
    

