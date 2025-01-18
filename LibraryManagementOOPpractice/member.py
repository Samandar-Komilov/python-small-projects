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