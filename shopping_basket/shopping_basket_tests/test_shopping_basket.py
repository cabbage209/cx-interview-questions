import pytest
from shopping_basket import Basket
from shopping_basket import Item
from shopping_basket import Pricer
from shopping_basket import Bonus

"""define the basket class which will hold the muteable
list of items and their subtotal"""


def test_default_basket():
    basket = Basket()
    assert basket.sub_total == 0.0
    assert basket.discount == 0.0
    assert basket.total == 0.0
    assert basket.items == []


@pytest.fixture
def empty_basket():
    return Basket()


"""define the Item class which holds a unique name,
 price and quantity for each item"""


def test_default_item():
    item = Item("fish", 2.0, 2)
    assert item.price == 2.0


@pytest.fixture
def gen_item():
    return Item("fish", 2.0, 2)


def test_add_item_success(empty_basket, gen_item):
    empty_basket.add_item(gen_item)
    assert len(empty_basket.items) == 2


def test_add_numerous_items(empty_basket):
    item = Item("fish", 2.10, 2)
    item1 = Item("crab", 1.02, 4)
    item2 = Item("shark", 4.31, 1)
    empty_basket.add_item(item, item1, item2)
    assert len(empty_basket.items) == 7
    assert empty_basket.sub_total == 12.59


# test that cannot be subtotal < 0.0
def test_basket_less_than_zero(empty_basket):
    item = Item("fish", -2.19, 2)
    empty_basket.add_item(item)
    assert empty_basket.sub_total == 0.0


@pytest.fixture
def full_basket(empty_basket):
    item = Item("fish", 2.10, 2)
    item1 = Item("crab", 1.02, 4)
    item2 = Item("shark", 4.31, 1)
    empty_basket.add_item(item, item1, item2)
    return empty_basket


# define the pricer class which calculates discount and total
def test_default_pricer(full_basket):
    Pricer(full_basket)
    assert full_basket.sub_total == 12.59
    # create offer buy 3 get 1 free on crab item
    assert full_basket.total == 11.57


@pytest.fixture
def bonus_basket(empty_basket):
    item = Item("fish", 2.1, 10)
    item1 = Item("crab", 1.00, 3)
    item2 = Item("shark", 5.00, 6)
    empty_basket.add_item(item, item1, item2)
    return empty_basket


def test_default_bonus(bonus_basket):
    Bonus(bonus_basket)
    assert bonus_basket.sub_total == 54.0
    # create bonus offer buy 2 get 1 free on fish and shark items
    assert bonus_basket.total == 37.7
