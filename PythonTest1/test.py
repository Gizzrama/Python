import random
n = random.randint(0, 100)

counter = 0

while True:
    guess = int(input("Guess a number between 0 and 100 within 5 attempts."))
    counter += 1
    if guess == n:
        print("Correct!")
        break
    
    elif guess > n:
        print("Enter lower number")
    
    elif guess < n:
        print("Enter higher number")
    
    else:
        print("Please enter a number between 0 and 100")
    
    if counter == 5:
        print("Try again!")
        break

print("This was the number:", n)
    
    

    
