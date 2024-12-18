
class User:
    def __init__(self):
        self.books = []

    def user_name(self, name):
        self.name = name

    @staticmethod
    def users_names():
        user1 = User("Gosia")
        user2 = User("Tomek")
        user3 = User("Radoslaw")
        user4 = User("Artur")
        user5 = User("Piotr")

        users = [user1, user2, user3, user4, user5]
        return users

    def borrowed_book(self, book):
        self.books.append(book)


    def count_books(self):
        count = len(self.books)
        return count

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)


    def display_books(self):
        for book in self.books:
            book.display_book_info()

class UserNotFoundError(Exception):
    pass


