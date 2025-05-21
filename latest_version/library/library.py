import json
import os
from .book import Book

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "library_data.json")

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
        print("book not found / already borrowed")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                self.save()
                print(f"You returned '{book.title}'")
                return
        print("book not found / not borrowed")
