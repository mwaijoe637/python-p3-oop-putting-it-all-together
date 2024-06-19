# testing/shoe_test.py

import pytest
from lib.shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", 42, "Black", "Leather")
    assert shoe.brand == "Nike"
    assert shoe.size == 42
    assert shoe.color == "Black"
    assert shoe.material == "Leather"
    assert shoe.is_worn == False

def test_wear_shoe():
    shoe = Shoe("Nike", 42, "Black", "Leather")
    shoe.wear()
    assert shoe.is_worn == True

def test_remove_shoe():
    shoe = Shoe("Nike", 42, "Black", "Leather")
    shoe.wear()
    shoe.remove()
    assert shoe.is_worn == False



