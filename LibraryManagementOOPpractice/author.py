class Author:
    def __init__(self, name, birthdate, nationality):
        self.name = name
        self.birthdate = birthdate
        self.nationality = nationality


    def __str__(self):
        return f"<Author: '{self.name}'>"