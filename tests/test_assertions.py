import pytest
def test_equals():
    assert 1 == 1
## def test_equals_fails ():
##    assert 1 == 2
def test_greater_than():
    assert 2 > 1
def test_less_than():
    assert 1 < 2
def test_not_equal():
    assert 1 != 2
def test_greater_or_equal():
    assert 2 >= 2
def test_less_or_equal():
    assert 1 <=2
def test_equals_tuple():
    assert (1,2) == (1,2)
def test_exists_in():
    assert 2 in [1,2,3]
def test_same_string():
    assert "abc" == "abc"
    