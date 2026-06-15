class BookNotAvailableError(Exception):
    def __init__(self, message, title):
        super().__init__(message)
        self.title = title

class InvalidReturnError(Exception):
    def __init__(self, message, title):
        super().__init__(message)
        self.title = title

class Book:
    def __init__(self, title, total_copies):
        self.__title = title
        self.__total_copies = total_copies
        self.__available_copies = total_copies

    def get_title(self):
        return self.__title

    def get_available_copies(self):
        return self.__available_copies

    def get_total_copies(self):
        return self.__total_copies        
    
    def set_total_copies(self, n):
        if n > 0:
            self.__total_copies = n
        else:
            print("Invalid: copies must be greater than 0")

    def borrow(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"Borrowed: {self.__title}. Copies left: {self.__available_copies}")
        else:
            raise BookNotAvailableError(f"No copies available for '{self.__title}'", self.__title)
        
    def return_book(self):
        if self.__available_copies < self.__total_copies:
            self.__available_copies += 1
            print(f"Returned: {self.__title}. Copies left: {self.__available_copies}")
        else:
            raise BookNotAvailableError(f"All copies of '{self.__title}' are already returned", self.__title)
        
book = Book("Clean Code", 2)
book.borrow()
book.borrow()

try:
    book.borrow()
except BookNotAvailableError as e:
    print("Error:", e)
    print("Book title from exception: ", e.title)

book.return_book()

try:
    book.return_book()
    book.return_book()
except InvalidReturnError as e:
    print("Error: ", e)