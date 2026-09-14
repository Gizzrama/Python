stationary = ["pencil", "eraser", "sharpener", "pen", "paper"]
value = [i.upper() for i in stationary]
print(value)

numbers = [1, 2, 5, 6, 10]
even = [i for i in numbers if i % 2 == 0]
print(even)

#Dictionary Comprehension
square = {i:i*i for i in numbers}
print(square)

length = {i:len(i) for i in stationary}
print(length)

#Zip

names = ["Srihari", "Harshal", "Arham"]
combination = list(zip(stationary, numbers, names))
print(combination)
