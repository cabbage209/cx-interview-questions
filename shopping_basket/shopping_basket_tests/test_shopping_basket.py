import pytest
from shopping_basket import Basket


def test_default_basket():
    basket = Basket()
    assert basket.sub_total == 0.0
    assert basket.discount == 0.0
    assert basket.total == 0.0
    assert basket.items == []

