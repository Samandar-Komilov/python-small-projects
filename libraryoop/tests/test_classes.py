import unittest
from libraryoop.classes import Book, Author, Member


class TestBook(unittest.TestCase):
    def setUp(self):
        self.author = Author(name="Author 1", birthdate="11/11/1991", nationality="Uzbek")
        self.book = Book(title="Book 1", author=self.author, isbn="ISBN122213", publication_year="2020")

    def test_string_repr(self):
        result = self.book.__str__()
        self.assertEqual(result, "<Book: 'Book 1'>")



if __name__ == "__main__":
    unittest.main()