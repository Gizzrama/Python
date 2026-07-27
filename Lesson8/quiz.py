import random

counter = 0
guess = random.randint(0, 10)


while True:
    number = int(input("Enter the number the computer has guessed"))

    if number == guess:
        print("Congratulations!")
        break
    
    counter = counter + 1
    
print(counter)
   




    