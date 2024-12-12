from users import User
from books import BookForAdults, BookForChildren


class Initializer:
    @staticmethod
    def init_users():
        user1 = User("Gosia")
        user2 = User("Tomek")
        user3 = User("Radoslaw")
        user4 = User("Artur")
        user5 = User("Piotr")

        users = [user1, user2, user3, user4, user5]

        return users

    @staticmethod
    def init_books():
        book1 = BookForAdults("The Chemistry of Death.", "Simon Beckett", 368,
                              True, "Synopsis", "Crime\n")
        book2 = BookForChildren("Pucio learns to speak.", "Marta Galewska-Kustra",
                                40, True, "synopsis", "0+\n")

        return [book1, book2]
