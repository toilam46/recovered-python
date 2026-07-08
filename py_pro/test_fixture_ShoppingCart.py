from ShoppingCart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    """ Create a fresh instance of ShoppingCart for each test."""
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item("Apple")
    assert cart.get_items() == ["Apple"]

def test_remove_item(cart):
    cart.add_item("Apple")
    cart.remove_item("Apple")
    assert cart.get_items() == []       

def test_remove_nonexistent_item(cart):
    cart.add_item("Apple")
    cart.remove_item("Banana")  # Removing an item that doesn't exist
    assert cart.get_items() == ["Apple"]

def test_get_items(cart):
    cart.add_item("Apple")
    cart.add_item("Banana")
    assert cart.get_items() == ["Apple", "Banana"]  