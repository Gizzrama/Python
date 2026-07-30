name = input("Enter anything: ").strip()

#Here we are trying to print a string in reverse order one by one e.g. cat --> t then a then c
#Recall that the len function stores the amount of characters in a string. Here we are trying to print name in reverse order.
#You may notice the name - 1. This is because indexing always starts from 0, and we need to reduce the length of the characters by 1 if we want to 
for i in range(len(name) - 1, -1, -1):
#This print statement uses indexing [i], which basically assigns a number for each character e.g. cat = 012. Also cat can be -3-2-1, starting from the right.
#Here we want to print each individual letter backwards. 
    print(name[i])

n = ""
for i in name:
    n = n + i

print(n)

n = ""
for i in name:
    n = i + n

print(n)