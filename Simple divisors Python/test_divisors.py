from divisors import divisors

def test_one():
    assert divisors(1) == [1]

def test_two():
    assert divisors(2) == [1, 2]

def test_three():
    assert divisors(3) == [1, 3]

def test_four():
    assert divisors(4) == [1, 2, 4]

def test_ten():
    assert divisors(10) == [1, 2, 5, 10]

def test_odd_number():
    assert divisors(11) == [1, 11]
