star = int(input("Enter the desired number of rows: "))

for i in range(0, star):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

#FLOYD'S TRIANGLE
rows = int(input("Enter the desired number of rows: "))
counter = 0
for i in range(0, rows):
    for j in range(0, i + 1):
        counter+=1
        print(counter, end=" ")
    
    print()

#DIAMOND
diamond = int(input("Enter the desired number or rows: "))

