#The while loop is used when you don't know how many times the code will repeat. In a for loop, you assign values inside the range, and the for loops essentially runs accordingly. 
#In a while loop however, it will keep running while the code is True. 
#This piece of code prints a number in reverse order e.g. User has entered the number 456, the output should be 654.
number = int(input("Enter any number greater than 0: "))
reverse = 0
#The while loop is saying that while the number is greater than 0, I will keep executing the code unless a condition is given.
while number >0:
    n = number%10 #--> The modulus operator provides the remainder of a number. It is divided by ten, so that we can get the last digit. E.g. if number 456%10, the result is 6.
    number = number//10 #--> Now we are left with the number 450, since 6 is the remainder. Floor division (//) rounds down a number. Here the number is 450, and floor division removes the 0 to get 45.
    reverse = reverse*10 + n 
    #The reverse variable has been assigned the value of 0 before the while loop. Now the reverse is getting incremented by a desired number.
    #We multiply by 10, and add n to get the first digit of the number. So for the first loop, it will be 0 = 0*10 + 6, which is 6. Now the 6 is placed in the hundreds slot rather than 4, reversing the order.
    #Second loop: We are left with 45. 45%10 = 40. result: 5. 40//10 = 4. Reverse equals 6 because of the first loop. So now, reverse = 6*10 + 5 = 65. 
    #Third Loop: We are left with only 4. 4%10 = 0. Result: 4. 0//10 = 0. Reverse equals 65 becuase of the second loop. So now, reverse = 65*10 + 4, which is equal to 654.
    #So this while loop reverses any number given by the user. The use of the number 456 was only an example.

    
print(f"The reverese of this number is {reverse}")
