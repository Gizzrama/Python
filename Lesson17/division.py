try:
    numerator, denominator = eval(input("Enter the numerator and hte denominator, separated by a comma"))
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

    
