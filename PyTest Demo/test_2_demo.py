import pytest

@pytest.mark.smoke
def test_CreditCard_minus():
    a = 30
    b = 50
    assert print(b - a) == 10,"Test is going to fail"

def test_CreditCard_string():
    a="Vicky"
    b="Vicky"
    assert a==b,"Test pass with string"