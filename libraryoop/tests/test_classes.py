import unittest
from libraryoop.classes import Book, Author, Member, Magazine


class TestBook(unittest.TestCase):
    def setUp(self):
        self.author = Author(name="Author 1", birthdate="11/11/1991", nationality="Uzbek")
        self.book = Book(title="Book 1", item_id=1, author=self.author, publication_year="2020")

    def test_set_wrong_isbn(self):
        with self.assertRaises(ValueError):
            self.book.set_isbn("invalid-isbn")
    
    def test_set_correct_isbn(self):
        self.book.set_isbn("978-0-306-40615-7")
        self.assertEqual(self.book.isbn, "978-0-306-40615-7")

    def test_string_repr(self):
        result = self.book.__str__()
        self.assertEqual(result, "<Book: 'Book 1'>")



class TestMagazine(unittest.TestCase):
    def setUp(self):
        self.author = Author(name="Author 1", birthdate="11/11/1991", nationality="Uzbek")
        self.magazine = Magazine(title="Magazine 1", item_id=1, issue_number=1122233, publisher=self.author)

    def test_string_repr(self):
        res = self.magazine.__str__()
        self.assertEqual(res, "<Magazine: 'Magazine 1'>")



class TestMember(unittest.TestCase):
    def setUp(self):
        self.author = Author(name="Author 1", birthdate="11/11/1991", nationality="Uzbek")
        self.book = Book(title="Book 1", item_id=1, author=self.author, publication_year="2020")
        self.member = Member(name="Member 1", member_id=1)

    def test_borrowed_books_tuple(self):
        self.assertTrue(isinstance(self.member.borrowed_books, tuple))

    def test_borrow_book(self):
        res = self.member.borrow_book(self.book)
        self.assertEqual(res, f"Book '{self.book}' borrowed successfully.")

    def test_return_book(self):
        self.member.borrow_book(self.book)
        res = self.member.return_book(self.book)
        self.assertEqual(res, f"Book '{self.book}' returned successfully.")

    def test_no_return_book(self):
        res = self.member.return_book(self.book)
        self.assertEqual(res, f"Book '{self.book}' was not borrowed by this member.")
    
    def test_has_borrowed(self):
        self.assertFalse(self.member.has_borrowed(self.book))
        self.member.borrow_book(self.book)
        self.assertTrue(self.member.has_borrowed(self.book))

    def test_string_repr(self):
        res = self.member.__str__()
        self.assertEqual(res, "<Member: 'Member 1'>")


if __name__ == "__main__":
    unittest.main()