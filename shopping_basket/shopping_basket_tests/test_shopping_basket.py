import pytest
from shopping_basket import Basket


def test_default_basket():
    basket = Basket()
    assert basket.sub_total == 0.0
    assert basket.discount == 0.0
    assert basket.total == 0.0
    assert basket.items == []

@pytest.fixture
def empty_basket():
    return Basket()

def test_add_item_success(empty_basket):
    empty_basket.add_item('fish', 2.0, 2)
    assert empty_basket.items == ['fish']

def test_add_item_fail(empty_basket):
    with pytest.raises(TypeError):
        empty_basket.add_item(3, 2.0, 2)
        

