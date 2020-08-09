class Book():
    isbn_counter = 9780000000000
    used_isbn = []

    def __init__(self, title, author, isbn=None):
        self.__title = title
        self.__author = author
        if isbn is None:
            isbn = Book.generate_isbn(self)
        if isbn is not None:
            isbn = str(isbn)
            test = self.check_isbn(isbn)
            if test == True:
                self.__isbn = isbn
                Book.used_isbn.append(str(self.__isbn))
            else:
                self.__isbn = Book.generate_isbn(self)

    @staticmethod
    def generate_isbn(self):
        self.isbn = self.isbn_counter
        while str(self.isbn) in Book.used_isbn:
            self.isbn = self.isbn_counter + 1
        return str(self.isbn)

    @staticmethod
    def check_isbn(string):
        if len(string) != 13:
            return False
        if not string.isalnum():
            return False
        if not string.startswith("978"):
            return False
        if string in Book.used_isbn:
            return False
        return True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn


book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling",9780747532743)
book2 = Book("My Story", "Max Muster")
book3 = Book("My Story Part 2", "Max Muster", 970)

print(book1.get_isbn()) # should print: 9780747532743
print(book1.get_title()) # should print: Harry Potter and the Philosopher's Stone
print(book1.get_author()) # should print: J. K. Rowling
print(book2.get_isbn()) # should print: 9780000000000
print(book3.get_isbn()) # should print: 9780000000001