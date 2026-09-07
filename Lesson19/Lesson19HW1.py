#You will create a marks analyser for a small class. The program will store student marks in a list, repeat a sample list, 
#find the number of marks, access selected values, slice and reverse the list, find matching marks using a loop, calculate the sum and average,
#and print the smallest and largest marks.

a = []
marks = [86, 93, 85, 97, 89]
print(marks)

sample_marks = [4, 7, 9, 2] * 2
print(sample_marks)

print(f"Number of marks", len(marks))
print(f"he first mark is {marks[0]}, and the final mark is {marks[-1]}")
print(f"The marks from the first one to the third one are {marks[0:3]}")

marks.reverse()
print(f"The reverse order of the marks is {marks}")

for i in range(len(marks) + 1):
    for j in len(i):
        if j[0] == j[1]:
            print("The number is a palindrome")

        else:
            print("The number is not a palindrome")

       




