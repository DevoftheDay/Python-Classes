class Book:
    def __init__(self, title, author):
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print("You have borrowed this book: ")

    def return_book(self):
        self.is_borrowed = False
        print("You have returned this book: ", )

book1 = Book("JK Rowling","Harry Potter" )
print(book1.title, book1.author)

