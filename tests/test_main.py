



# basic tests

def sum(a: int, b: int):
    return a + b

def test_sum_positive_numbers():
    assert sum(3, 2) == 5

def test_sum_negative_numbers():
    assert sum(-1, -1) == -2

def test_sum_zeros():
    assert sum(0, 0) == 0