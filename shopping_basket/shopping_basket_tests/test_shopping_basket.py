import pytest
from shopping_basket import Basket
from shopping_basket import Item
from shopping_basket import Pricer


def test_default_basket():
    basket = Basket()
    assert basket.sub_total == 0.0
    assert basket.discount == 0.0
    assert basket.total == 0.0
    assert basket.items == []

@pytest.fixture
def empty_basket():
    return Basket()

def test_default_item():
    item = Item('fish', 2.0, 2)
    assert item.price == 2.0

@pytest.fixture
def gen_item():
    return Item('fish', 2.0, 2)

    
def test_add_item_success(empty_basket, gen_item):
    empty_basket.add_item(gen_item)
    assert len(empty_basket.items) == 2

def test_add_numerous_items(empty_basket):
    item = Item('fish', 2.10, 2)
    item1 = Item('crab', 1.02, 4)
    item2 = Item('shark', 4.31, 1)
    empty_basket.add_item(item, item1, item2)
    assert len(empty_basket.items) == 7
    assert empty_basket.sub_total == 12.59

@pytest.fixture
def full_basket(empty_basket):
    item = Item('fish', 2.10, 2)
    item1 = Item('crab', 1.02, 4)
    item2 = Item('shark', 4.31, 1)
    empty_basket.add_item(item, item1, item2)
    return empty_basket

    
def test_default_pricer(full_basket):
    pricer = Pricer(full_basket)
    #assert full_basket.sub_total == 13.0
    