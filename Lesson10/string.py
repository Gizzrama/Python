name = input("Enter anything: ").strip()

#Here we are trying to print a string in reverse order one by one e.g. cat --> t then a then c
#Recall that the len function stores the amount of characters in a string. Here we are trying to print name in reverse order.
#You may notice the name - 1. This is because indexing always starts from 0, and we need to reduce the length of the characters by 1 if we want to 
for i in range(len(name) - 1, -1, -1):
#This print statement uses indexing [i], which basically assigns a number for each character e.g. cat = 012. Also cat can be -3-2-1, starting from the right.
#Here we want to print each individual letter backwards.
#So since the i gets incremented by -1 in this for loop, and because the indexing will start from the right, the name will be printed in reverse.
    print(name[i])

#Since n has been assigned a string value, you can't just give 0, since it will get concatenated. So you just give an empty slot, so the string gets incremented.
#This for loop will print the name from left to right. The i in name means the indexes in the name (0, 1, 2, 3 etc.)
#The n = n + i basically states 'Place an index value to the right of n'. Since n is a string, it cannot just simply add up. It combines together to form a sequence of characters.
n = ""
for i in name:
    n = n + i

print(n)

#The same is applied to this loop. If you write n = i + n, it means 'Place an index value to the left of n', and thus prints the name in reverse order as a whole string.
#e.g. Let's say the user entered the name Joe. Now since n = "", basically nothing, if you place i to the left of n, you will get 0 "". Now the indexing for 'Joe' is 012. So 0 will get printed to the left of "". So it will look like J "". Now this is repeated since the i is incremented by 1 each time, and print the name Joe as oeJ. 

n = ""
for i in name:
    n = i + n

print(n)