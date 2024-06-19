# testing/book_test.py

import pytest
from lib.book import Book

def test_book_initialization():
    book = Book("1984", "George Orwell", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.pages == 328
    assert book.current_page == 1

def test_turn_page():
    book = Book("1984", "George Orwell", 328)
    book.turn_page(100)
    assert book.current_page == 100

def test_turn_page_out_of_range():
    book = Book("1984", "George Orwell", 328)
    with pytest.raises(ValueError):
        book.turn_page(500)

# Additional tests...

