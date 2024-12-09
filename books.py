from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, pages, available, synopsis):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available
        self.synopsis = synopsis

    def display_common_book_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Pages: {self.pages}')
        print(f'Available? {"Yes" if self.available else "No"}')
        print(f'Synopsis: {self.synopsis}')

    @abstractmethod
    def display_book_info(self):
        pass


class BookForAdults(Book):
    def __init__(self, title, author, pages, available, synopsis, genre):
        super().__init__(title, author, pages, available, synopsis)
        self.genre = genre


    def display_book_info(self):
        super().display_common_book_info()
        print(f'Genre: {self.genre}')


class BookForChildren(Book):
    def __init__(self, title, author, pages, available, synopsis, age):
        super().__init__(title, author, pages, available, synopsis)
        self.age = age

    def display_book_info(self):
        super().display_common_book_info()
        print(f'Age: {self.age}')