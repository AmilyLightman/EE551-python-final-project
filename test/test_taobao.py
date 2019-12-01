import pytest
from taobao_test import AutoBuy

def test_main():
    my_buy = AutoBuy()
    assert(my_buy.run())
