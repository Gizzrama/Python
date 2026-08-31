number = [5, 7, 11, 2, 6, 8]

sum = 0
for i in range(len(number)):
    sum += number[i]

print("The sum of all the numbers is", sum)
print("The average of all the numbers is", sum/len(number))

count = 0
for i in number:
    count = count + i


number.sort()
print("The smallest number in the list is", number[0])
print("The largest number in the list is", number[-1])