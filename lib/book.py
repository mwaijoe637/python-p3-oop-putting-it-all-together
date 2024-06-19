# lib/book.py

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
    
    def open(self):
        self.current_page = 1
    
    def turn_page(self, page):
        if 1 <= page <= self.pages:
            self.current_page = page
        else:
            raise ValueError("Page out of range")
    
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    # Properties using the property() function
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        self._title = title
    
    title = property(get_title, set_title)
    
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if not author:
            raise ValueError("Author cannot be empty")
        self._author = author
    
    author = property(get_author, set_author)

    def get_pages(self):
        return self._pages
    
    def set_pages(self, pages):
        if pages <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = pages
    
    pages = property(get_pages, set_pages)

    def get_current_page(self):
        return self._current_page
    
    def set_current_page(self, current_page):
        if 1 <= current_page <= self.pages:
            self._current_page = current_page
        else:
            raise ValueError("Current page out of range")
    
    current_page = property(get_current_page, set_current_page)
