from abc import ABC, abstractmethod

class Books(ABC):
    def __init__(self, category, title, author, pages, available, synopsis):
        self.category = category
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available
        self.synopsis = synopsis

    @abstractmethod
    def display_concrete_info(self):
        pass

    def display_info_book(self):
        print(f"Category: {self.category}")
        print(f"Title: {self.title}")
        print(f"Author: {self.title}")
        print(f"Pages: {self.pages}")
        self.display_concrete_info()
        print(f"Available? {'Yes' if self.available else 'No'}")
        print(f"Synopsis: {self.synopsis}")


class BooksForChildren(Books):
    def __init__(self, category, title, author, pages, available, synopsis, age):
        super().__init__(category, title, author, pages, available, synopsis)
        self.age = age

    def display_concrete_info(self):
        print(f"Age: {self.age}")


class BooksForAdults(Books):
    def __init__(self, category, title, author, pages, available, synopsis, genre):
        super().__init__(category, title, author, pages, available, synopsis)
        self.genre = genre


    def display_concrete_info(self):
        print(f"Genre: {self.genre}")

class BookNotFoundError(Exception):
    pass

class BookNotAvailableError(Exception):
    pass

class ToManyBooks(Exception):
    pass
