#You will create a marks analyser for a small class. The program will store student marks in a list, repeat a sample list, 
#find the number of marks, access selected values, slice and reverse the list, find matching marks using a loop, calculate the sum and average,
#and print the smallest and largest marks.

print("---MARKS SUMMARY---")
print("\n")
choice = eval(input("Enter any five two-digit numbers separated by a comma:"))
marks = list(choice)
print(marks)
for i in choice:
    if len(str(i)) != 2:
        print("Invalid number. Enter a two-digit number. Please try again")

for j in range(len(marks)):
    if j > 4:
        print('Please enter exactly five numbers. Please try again.')


print(f"Number of marks", len(marks))
print(f"The first mark is {marks[0]}, and the final mark is {marks[-1]}")
print(f"The marks from the first one to the third one are {marks[0:3]}")

marks.reverse()
print(f"The reverse order of the marks is {marks}")


counter = 0
for i in marks:
    if i % 11 == 0:
        counter += 1

print("Numbers which have the same first and last digits:", counter)

end_loop = 0
counter = 0
for i in marks:
    counter += i

    if end_loop >= 5:
        break
print("The sum of all the marks is", counter)
print("The average of all the marks is", counter/5)

marks.sort()

print("The lowest mark is", marks[0])
print("The highest mark is", marks[4])




    








 






       




