n = int(input("How many rows of * do you want to print?"))
c = int(input("How many columns of * do you want to print?"))

for i in range(n):
    for j in range(c):
        print("*", end="     ")
    print() 