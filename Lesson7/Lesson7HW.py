
print("ASCII String Value Checker")

#print(ord("b")) --> The ord
#print(ord("5"))

#print(chr(78))
#print(chr(90))

character = input("Enter a single character: ").strip()

if type(character) is str or int and len(character) == 1:
    print("Valid input")
        
    ascii_value = ord(character)
    print(f"Character: {character} \nASCII Value: {ascii_value}")


    if ascii_value >= 48 and ascii_value <= 57:
        print("This is a digit")

    elif ascii_value >= 65 and ascii_value <= 90:
        print("This is an uppercase letter")

    elif ascii_value >= 97 and ascii_value <= 122:
        print("This is a lowercase letter")

    elif ascii_value == 32:
        print("This is the spacebar")

    else:
        print("It is a special character")

else:
    print("Enter only one character. Try again")