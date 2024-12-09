class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book):
        self.books.append(book)

    def return_book(self):
        pass