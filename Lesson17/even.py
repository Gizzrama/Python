#This is exception handling
#An exception is an unusual condition that interrupts a program's normal flow, stopping the rest of the code from running. 
#It's different from a syntax error, which happens before the program even starts, because an exception occurs while the program is actually running.
#Essentially exception handling is preventing errors from occurring in a piece of code.

#The try and except keywords are conditional statements, that run code based on if the condition is True or false.
#The try keyword handles risky code, which might result in an error. You write whatever code you want to write inside the try block, and the try block holds the risky code.
#Just like if-else statements, except needs try, but try doesn't need except. The try block can run without except. This is because the try block is like checking 
#the risky code for any errors, and the except block needs this to sabotage any errors. But the try block doesn't need the except block, since it just stores risky
#code, and doesn't deal with errors.

#Line 18: valid is set to False, since 'We are not successful yet'. Remember False always has a value even if it is assigned to a variable, since it is a boolean. 
#         However if False is written with a lower-case f, then it is undefined, so if I write valid = false, the false has no value before it is assigned to valid.
#Line 19: while not valid ensures that while loop is not false, thus while True
#Line 23: valid is set to True, which breaks the loop. Note that 'while not valid:' is not the same as 'valid = True'. *Explained at the end*
#Line 31: except can sabotage a certain type of error in python, or just all errors in general, like in Line 30 & 33 respectively.
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
    

#while True: the condition is the literal keyword True, hardcoded directly into the loop. 
#            Every single time Python checks it, there's nothing to compute — it's already True. 
#            It can never be anything else, because there's no variable involved, nothing to change.

#while not valid: the condition is an expression that Python has to compute fresh each time, based on whatever valid equals at that instant. 
#                 On the first check, it happens to compute to True — sure. But that's just what it evaluated to given the current state of valid.
#                 'The next time through, Python doesn't reuse that old answer — it recalculates not valid from scratch, using whatever valid is now.
#So that means during the first loop, valid = False --> while not valid --> while not False --> while True
#The result might be the same, however while True is hardcoded directly into the loop and while not valid has to check the state of valid after each loop.

#valid = True
#This changes the state of valid to True. But how does it actually break the loop since while not valid is also equal to True, and valid is also updated to True?
#while not valid becomes while True. It has to check the state of valid each loop, and either continue or break. 
#When valid = True, it becomes valid = True --> while not valid --> while not True --> while False, and thus breaks the loop
#Another way to think about is that valid = True states that the exception handling was successful.
#So at the start the exception handling was not successful (valid = False). Then it became successful (valid = True)


#*FOR INFO ON TYPES OF ERRORS AND MORE, CHECK division.py*