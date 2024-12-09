import sys
from books import BookForAdults, BookForChildren

def display_library_books():
    book1 = BookForAdults("The Chemistry of Death.", "Simon Beckett", 368,
                          True, "Synopsis", "Crime\n")
    book2 = BookForChildren("Pucio learns to speak.", "Marta Galewska-Kustra",
                             40, True, "synopsis", "0+\n")

    book1.display_book_info()
    book2.display_book_info()

if __name__ == "__main__":
    while True:
        print("1. View a list of your books.")
        print("2. View a list of books in your library.")
        print("3. Borrow a book.")
        print("4. Return a book.")
        print("5. Exit program.")

        try:
            option = int(input("Type option(1, 2, 3, 4 or 5): \n"))
            if option not in [1, 2, 3, 4, 5]:
                raise Exception
        except Exception:
            print("Incorrect command. Try again.\n")


        if option == 1:
            pass
        elif option == 2:
            display_library_books()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            sys.exit()