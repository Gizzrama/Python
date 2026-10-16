#Prompt: Build a simple library system using a class. Each book is an object. 
#Your system lets users borrow and return books and tracks whether each book is currently available.

class Book:
    
    def __init__ (self, title, author):
        self.t = title
        self.a = author
        self.ib = False

    def borrow(self):
        self.ib = True
        print("You have borrowed", self.t)

    def return_book(self):
        self.ib = False
        print("You gave returned", self.t)


pj = Book("Percy Jackson", "Rick Riordan")
pj.borrow()

hp = Book("Harry Potter", "JK Rowling")
hp.return_book()

book = Book("A Rover's Story", "Jasmine Warga")
book.return_book()


    

        