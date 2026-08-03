n = int(input("Enter the number of rows: "))

counter = 0
for i in range(n):
    for j in range(0, i + 1):
       counter += 1
       print(counter, end= " ")
    print()

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(0, i + 1):
        print(i + 1, end = " ")
    
    print()
