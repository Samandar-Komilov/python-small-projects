from abc import ABC, abstractmethod


############ ABSTRACT CLASSES ############

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id


    @abstractmethod
    def __str__(self):
        pass



########### CONCRETE CLASSES ############

class Book(LibraryItem):
    def __init__(self, title, item_id, author, isbn="", publication_year=""):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    
    def __str__(self):
        return f"<Book: '{self.title}'>"
    


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, publisher):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publisher = publisher

    
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
        self.borrowed_books = []
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        return self.borrowed_books
    
    def return_book(self, book):
        self.borrowed_books.remove(book)
        return self.borrowed_books

    
    def __str__(self):
        return f"<Member '{self.name}'>"