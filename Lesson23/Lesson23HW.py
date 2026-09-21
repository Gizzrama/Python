#You will create a simple library checker. The program stores book names and copy counts, builds a library stock dictionary, filters books that are available, 
#asks the reader which book they want to borrow, stops if the book is unavailable, updates late fees, reduces the copy count, and prints a final summary.

library = {
    "Macbeth":0,
    "Life of Pi":4,
    "The Book Thief":6,
    "Animal Farm":0,
    "Cat's Cradle":3
}


while True:
    choice = int(input("Enter 0 to borrow 'Macbeth' by Shapespeare, 1 for 'Life of Pi' written by Yann Martel, 2 for 'The Book Thief', written by Markus Zusak, 3 'Animal Farm' by George Orwell and 4 for 'Cat's Cradle', written by Kurt Vonnegut. Enter 100 to stop borrowing."))

    for i in library:
        print(library[i])
        

    