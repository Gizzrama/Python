import random
guess = random.randint(0, 9)

print("The system will print a number from 0 to 9, and you will have to guess it.")
print("You will have five attempts to guess the number")
counter = 0
while True:
    counter += 1
    number = int(input("Enter a number between 0 and 9"))

    if number == guess:
        print("That is correct!")
        print(guess)
        break

    elif counter >= 5:
        print("Uh oh. Out of guesses. Please try again.")
        break
    
    else:
        print("That wasn't quite right. Try again")