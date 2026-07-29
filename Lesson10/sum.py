n = int(input("Enter any number: "))


#This for loop is asking for all the numbers from 0 to n to printed. Since the stop is always exclusive, we add 1 to n if we want n to be printed.
for i in range(0, n+1):
    print(i)

print("\n")

#This is where it gets interesting. This for loop is asking for the sum of all numbers from 0 to n inclusive. 
#The sum is a function that adds up all the numeric items in an iterable (such as a list, tuple, set or dictionary), and returns the total.
#For now the sum has been assigned the value 0.
sum = 0
#Let's say the user entered 20 as the value of n. Now since the i gets incremented by 1 each loop, the equation becomes 1 = 0 + 1 (sum  = sum + 1). So the sum of the first loop (0 + 1) is 1.
#Now for the second loop, we are looking at the sum of 1 and 2. Since the sum value has been updated to 1 now, the equation becomes: 3 = 1 + 2 since the i is incremented by 1 each loop. This is the second loop, thus i is 2.
#Now for the third loop, we are looking at the sum of all the numbers from 0, 1 & 2 (which is 3) and the next number (3). The sum value has been update to 3 now, thus
#the equation becomes 6 = 3 + 3 (sum = sum + i).
#Basically the sum gets updated after each loop and keeps track of the sum of all numbers until the loop is repeated 20 times. (Because we want the sum of all the numbers from 0 - 20).

for i in range(0, n+1):
    sum = sum + i

print(sum)
 #So since the user entered 20 as the value of n, the first for loop will count all the numbers from 1 - 20, and will find the sum of all the numbers from 0 - 20 (210) in the second for loop.

    
  