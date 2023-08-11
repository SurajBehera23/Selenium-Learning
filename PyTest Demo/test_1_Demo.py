import pytest

@pytest.mark.xfail
def test_firstprogram():
    print("SURAJ")

def test_CreditCard_Sum():
    a=10
    b=10
    c=a+b
    assert c==20,"sum complete"