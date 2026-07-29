#LOOPS - A loop is a control flow structure used to repeat a specific block of code multiple times without rewrtiting it. 
#There are three types of loops: for loop, while loop and a nested. This lesson we will be exploring the for loop, and when, why and how it is used.
#We will also assess its behaviour and characteristics.
n = int(input("Enter any number: "))

#The for loop is used to repeat a certain block of code a certain amount of times given by the programmer.
#The 'i' is a standard variable name used as a temporary placeholder, most commonly representing an index, iterator or integer inside loops.
#The i has a predefined value of 0. In a for loop, the i is incremented by a value given by the user. The value is always the last number inside the range function. Here, it is -1, so the i decreases by 1 each time.
#The range function generates an immutable sequence of numbers. It is basically range(start, stop, step). The start is inclusive, and the default value if the programmer doesn't enter anything will be 0. The stop is where the numbers will end, and is exclusive. It must be entered by the programmer. The step is the increment (By how much the numbers will increase or decrease by), and if no value has been entered by the programmer, the default value is 1.
#In this scenario, the user is basically asking for any number to be entered (n), and the user wants to count all the numbers from n to 1 decreasing by 1 each time. 
#The second 1 is basically the target. The for loop will count all numbers from n to 1, and 1 is exclusive. So the for loop will print numbers from n to 2 inclusive.
for i in range(n, 1, -1):
    print(i)


