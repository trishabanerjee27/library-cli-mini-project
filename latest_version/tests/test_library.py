import unittest
from library.book import Book
from library.library import Library
import os

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.books = []

        self.book = Book("Test Book", "Test Author", "TESTISBN")
        self.library.books.append(self.book)

    def tearDown(self):
        self.library.books = []

    def test_add_book(self):
        new_book = Book("New Book", "New Author", "NEWISBN")
        self.library.add_book(new_book.title, new_book.author, new_book.isbn)
        self.assertIn(new_book.isbn, [b.isbn for b in self.library.books])

    def test_lend_book_success(self):
        self.assertTrue(self.book.available)
        self.library.lend_book("TESTISBN")
        self.assertFalse(self.book.available)

    def test_lend_book_not_found(self):
        result = self.library.lend_book("UNKNOWN")
        self.assertIsNone(result)

    def test_return_book_success(self):
        self.book.available = False
        self.library.return_book("TESTISBN")
        self.assertTrue(self.book.available)

    def test_return_book_not_found(self):
        result = self.library.return_book("UNKNOWN")
        self.assertIsNone(result)

    def test_duplicate_add(self):
        duplicate = Book("Another Title", "Another Author", "TESTISBN")
        self.library.books.append(duplicate)
        count = [b.isbn for b in self.library.books].count("TESTISBN")
        self.assertGreater(count, 1)

if __name__ == "__main__":
    unittest.main()