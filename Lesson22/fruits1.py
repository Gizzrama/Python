import array as arr
fruits = arr.array('i', [1, 2, 3, 4])
print("The numbers in the array are", fruits)

fruits.append(5)
print("The numbers in the array are", fruits)

fruits.insert(3, 6)
print("The numbers in the array are", fruits, "and there is a new number at index 1")

fruits.reverse()
print("The reversed order of the numbers in the array is", fruits)