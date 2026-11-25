class Library:
    def __init__(self):
        self.__book = []
        
        
    def add__book(self, title):
        self.__book.append(title)
        
        
    def remove__book(self, title):
        self.__book.remove(title)
        
        
    def list__books(self):
        print(self.__book)
        

l = Library()

l.add__book("java")
l.add__book("python")
l.add__book("C++")


l.add__book("java")
l.list__books()
    