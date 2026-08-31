number = [1, 6, 7, 2]
print(number)

print(number[0])
number.append(96)
number.append(104)

print(number)

print(number[2:5])
print(number[3:6])

print("The length of the list is", len(number))

for i in range(len(number)):
    print(i, number[i])

number.reverse()
print(number)

number.sort()
print(number)

number.remove(104)
print(number)

number.pop()
print(number)

