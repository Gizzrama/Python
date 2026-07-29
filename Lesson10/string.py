name = input("Enter anything: ").strip()

#Here we are trying to print a string in reverse order one by one e.g. cat --> t then a then c
#Recall that the len function stores the amount of characters in a string. Here we are trying to print name in reverse order 
for i in range(len(name) - 1, -1, -1):
    print(name[i])

n = ""
for i in name:
    n = n + i

print(n)

n = ""
for i in name:
    n = i + n

print(n)