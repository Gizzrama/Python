n = int(input("How many rows of * do you want to print?"))

for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end =" ")
    print()