n = int(input("How many rows of * do you want to print?"))
#counter = 0


for i in range(0, n):
    #counter = counter + 1
    for j in range(0, i + 1):
        print("*", end =" ")
    print()