try:
    number = int(input("Enter a number: "))
    print("The number entered is ", number)

except ValueError as e:
    print("There is an exception", e)

except:
    print("There is an exception")