a = [5, 4, 7, 2, 11, 10]

target = 7

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print("Element found")
            break