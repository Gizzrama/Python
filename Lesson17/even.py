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
    

