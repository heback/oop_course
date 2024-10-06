class Book:
    def __init__(self, title, author, published_year, isbn):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print(f"Found: {book.title} by {book.author}")
                return book
        print("Book not found.")
        return None

# 실행 예시
book1 = Book("1984", "George Orwell", 1949, "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")

lib = Library()
lib.add_book(book1)
lib.add_book(book2)

book1.borrow_book()
book1.return_book()
lib.find_book_by_isbn("1234567890")
