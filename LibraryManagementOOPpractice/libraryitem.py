from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id


    @abstractmethod
    def __str__(self):
        pass