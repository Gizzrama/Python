#Prompt: You will create a fun calculator that first generates a lucky number and a random activity. Then the program runs a small number guessing game. 
#After that, it asks for numbers and uses math functions to find ceiling value, floor value, copied sign value, absolute value, and GCD. 
#At the end, it prints a clear summary of the random results.

import random, math

print("---GUESSING GAME---")
print("\n")
print("This is a fun number guessing game, where the computer will pick a number and you will have 5 attempts to guess it.")
counter = 0
while True:
    counter += 1
    number = random.randint(1, 20)
    guess = int(input("Guess a number between 1 & 20: "))

    if guess > number:
        print(f"The number is less than {guess}")
        

    elif guess < number:
        print(f"The number is less than {guess}")
    
    elif guess == number:
        print("That's correct!")
        print("\n")
        break
    
    else:
        pass
    
    if counter >= 5:
        print("Out of guesses. Try again.")
        break
    
    else:
        pass


print("---NUMBER INFORMATION---")
print("\n")
print("In this game, you will pick a number and the computer will tell you some interesting facts about the number.")

n = int(input("Pick any whole number: "))
y = int(input("Pick another whole number: "))
print(f"The nearest whole number upper bound limit for {n} is {math.ceil(n)}")
print(f"The nearest whole number lower bound limit for {n} is {math.floor(n)}")
print(f"The square root of {n} is {math.sqrt(n)}")
print(f"The copysign value for {n} and {y} is {math.copysign(n, y)}")
print(f"The Highest Common Factor (HCF) for {n} and {y} is {math.gcd(n, y)}")
print(f"The absolute value for {n} is {math.fabs(n)}")




