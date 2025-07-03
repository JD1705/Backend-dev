# basic tests

def sum(a: int, b: int):
    return a + b

def test_sum_positive_numbers():
    assert sum(3, 2) == 5

def test_sum_negative_numbers():
    assert sum(-1, -1) == -2

def test_sum_zeros():
    assert sum(0, 0) == 0

# practice with another function

def multi(num_1: int, num_2: int):
    return num_1 * num_2

# test must begin with test_*

def test_positive_numbers():
    assert multi(2,3) == 6
    
def test_positive_and_zero():
    assert multi(3, 0) == 0
    
def test_one_positive_and_negative():
    assert multi(2,-3) == -6