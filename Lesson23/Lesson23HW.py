#You will create a simple library checker. The program stores book names and copy counts, builds a library stock dictionary, filters books that are available, 
#asks the reader which book they want to borrow, stops if the book is unavailable, updates late fees, reduces the copy count, and prints a final summary.

library = {
    "Macbeth":0,
    "Life of Pi":4,
    "The Book Thief":6,
    "Animal Farm":0,
    "Cat's Cradle":3
}

for title, copies in library.items():
    print(f"Copies left for {title}: {copies}")

print("Each book costs $3")
cost = 0
book_count = 0
while True:
    choice = int(input("\nEnter 1 to borrow 'Macbeth' by Shapespeare, 2 for 'Life of Pi' written by Yann Martel, 3 for 'The Book Thief', written by Markus Zusak, 4 'Animal Farm' by George Orwell and 5 for 'Cat's Cradle', written by Kurt Vonnegut. Enter 100 to stop borrowing."))

    if choice == 1:
        print("Out of stock")
        continue

    elif choice == 2:
        print("You have borrowed Life of Pi")
        book_count += 1
        cost += 3

    elif choice == 3:
        print("You have borrowed The Book Thief")
        book_count += 1
        cost += 3

    elif choice == 4:
        print("Out of stock")
        continue

    elif choice == 5:
        print("You have borrowed Cat's Cradle")
        book_count += 1
        cost += 3

    elif choice == 100:
        confirm = input("Would you like to end purchase? Click yes or no:").strip().lower()
        if confirm == "yes":
            print("--Loop Ended--")
            break

        else:
            continue

    else:
        print("Invalid number")


print("\nBooks Bought:", book_count)
print(f"Total Cost: ${cost}")