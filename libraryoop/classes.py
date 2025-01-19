from abc import ABC, abstractmethod


############ ABSTRACT CLASSES ############


class Borrowable(ABC):
    @abstractmethod
    def borrow(self, member):
        pass

    @abstractmethod
    def return_item(self, member):
        pass



class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id


    @abstractmethod
    def __str__(self):
        pass



########### CONCRETE CLASSES ############

class Book(Borrowable, LibraryItem):
    def __init__(self, title, item_id, author, publication_year=""):
        super().__init__(title, item_id)
        self.author = author
        self.__isbn = None
        self.__pages = 0
        self.publication_year = publication_year
    @property
    def isbn(self):
        return self.__isbn

    
    @isbn.setter
    def isbn(self, val):
        if self.is_valid_isbn(val):
            self.__isbn = val
        else:
            raise ValueError("Invalid ISBN format")
        
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, val):
        if val > 0:
            self.__pages = val

    def borrow(self, member):
        member.borrow_book(self)

    def return_item(self, member):
        member.return_book(self)

    @staticmethod
    def is_valid_isbn(isbn):
        isbn = isbn.replace("-", "").replace(" ", "")
        return Book.is_valid_isbn10(isbn) or Book.is_valid_isbn13(isbn)
        
    @staticmethod
    def is_valid_isbn10(isbn):
        if len(isbn) != 10:
            return False
        
        sum = 0
        for i in range(9):
            if not isbn[i].isdigit():
                return False
            sum += int(isbn[i]) * (10 - i)
        
        if isbn[9] == 'X':
            sum += 10
        elif isbn[9].isdigit():
            sum += int(isbn[9])
        else:
            return False
        
        return sum % 11 == 0

    @staticmethod
    def is_valid_isbn13(isbn):
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        
        sum = 0
        for i in range(12):
            sum += int(isbn[i]) * (1 if i % 2 == 0 else 3)
        
        check_digit = (10 - (sum % 10)) % 10
        
        return int(isbn[12]) == check_digit
    
    # Magic methods
    def __eq__(self, other):
        return self.isbn == other.isbn
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"<Book: '{self.title}'>"
    


class Magazine(Borrowable, LibraryItem):
    def __init__(self, title, item_id, issue_number, publisher):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publisher = publisher
    
    def borrow(self, member):
        return member.borrow_book(self)

    def return_item(self, member):
        return member.return_item(self)
    
    def __str__(self):
        return f"<Magazine: '{self.title}'>"
    


class Author:
    def __init__(self, name, birthdate, nationality):
        self.name = name
        self.birthdate = birthdate
        self.nationality = nationality


    def __str__(self):
        return f"<Author: '{self.name}'>"
    


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []

    @property
    def borrowed_books(self):
        return tuple(self.__borrowed_books)
    
    def borrow_book(self, book):
        if book not in self.__borrowed_books:
            self.__borrowed_books.append(book)
        return f"Book '{book}' borrowed successfully."
    
    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            return f"Book '{book}' returned successfully."
        return f"Book '{book}' was not borrowed by this member."
    
    def has_borrowed(self, book):
        return book in self.borrowed_books
    
    def __str__(self):
        return f"<Member: '{self.name}'>"