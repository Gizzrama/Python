#ASCII is a standardized character encoding system that assigns a unique number between 0 and 127 to English letters, 
#digits, and symbols to ensure universal text compatibility across different computers. It acts as a critical middleman, 
#translating human-typed letters into decimal numbers that software can easily organize. While binary is the raw, foundational 
#language of 1s and 0s that hardware processes, ASCII serves as the rulebook that gives those binary sequences their specific text
#meanings. Today, this system is widely used in computer programming source files, network communication protocols, and as the 
#structural foundation for modern Unicode and emojis.
print("ASCII String Value Checker")

#print(ord("b")) --> The ord() function returns the ASCII value for a character
#print(ord("5")) --> The chr() function converts an ASCII value into a character

#print(chr(78))
#print(chr(90))

character = input("Enter a single character: ").strip()

#len() is a function in python which checks the amount of characters in a string or an integer. It does not do the same for float.
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

#ASCII Ranges
# 65 - 90: A - Z (uppercase)
# 97 - 122: a - z (lowercase)
# 48 - 57: 0 - 9 (digits)
# 32: Spacebar
# Everythin else: Special characters