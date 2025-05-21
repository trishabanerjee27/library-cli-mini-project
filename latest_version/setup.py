import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "library_data.json")

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["isbn"], data["available"])

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]

    def save(self):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)


    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save()

    def list_books(self):
        if not self.books:
            print("no books in the library")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                self.save()
                print(f"you borrowed '{book.title}'")
                return
        print("book NOT found / could be already borrowed")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                self.save()
                print(f"You returned '{book.title}'")
                return
        print("book NOT found or wasn't borrowed.")

