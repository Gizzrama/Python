#Prompt: Build a grade book that stores student names and scores in a dictionary. 
#Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

#Step 1
grade_book = {
    "John":98,
    "James":99,
    "Alice":95,
    "Ben":93,
    "Caitlyn":89
}

#Step 2
sum = 0
for i in grade_book:
    sum = sum + grade_book.get(i)

print("The average score is:", sum/len(grade_book))

#Step 3
a = max(grade_book.values())
b = min(grade_book.values())

for i in grade_book:
    if grade_book[i] == a:
        print("The top scorer is", i)

    elif grade_book[i] == b:
        print("The bottom scorer is", i)



#Step 4
while True:
    choice = int(input("Enter 0 for John's report, 1 for James's report, 2 for Alice's report, 3 for Ben's report and 4 for Caitlyn's report. Enter 5 to exit the loop"))
    if choice == 0:
        print(grade_book.get("John"))

    elif choice == 1:
        print(grade_book.get("James"))

    elif choice == 2:
        print(grade_book.get("Alice"))

    elif choice == 3:
        print(grade_book.get("Ben"))

    elif choice == 4:
        print(grade_book.get("Caitlyn"))

    else:
        print("--End Loop--")
        break


