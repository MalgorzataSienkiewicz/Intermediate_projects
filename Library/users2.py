from books2 import BookNotFoundError
class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    @staticmethod
    def users_names():
        user1 = User("Gosia")
        user2 = User("Tomek")
        user3 = User("Radoslaw")
        user4 = User("Artur")
        user5 = User("Piotr")

        users = [user1, user2, user3, user4, user5]
        return users

    def borrow_book(self, book):
        self.books.append(book)


    def count_books(self):
       return len(self.books)

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        raise BookNotFoundError(f"Book '{title}' not found in user's borrowed list.")


    def display_books(self):
        if not self.books:
            print("No books borrowed.")
        else:
            print(f"Books borrowed by {self.name}:")
            for book in self.books:
                book.display_book_info()

class UserNotFoundError(Exception):
    pass


