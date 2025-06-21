from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

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
    
# API tests require TestClient

def test_status_code():
    response = client.post('/sum/?a=4&b=2')
    print(response.json())
    assert response.status_code == 200
    
def test_sum_response():
    response = client.post('/sum/?a=4&b=2')
    assert response.json()['result'] == 6
    
def test_sum_plus_none_raise_exception():
    response = client.post('/sum/?a=4')
    print(response.json())
    assert response.status_code == 400
    assert response.json()['detail'] == 'all parameters must be passed to'
    
def test_if_parameters_are_none_raise_exception():
    response = client.post('/sum/')
    print(response.json())
    assert response.status_code == 400
    assert response.json()['detail'] == 'all parameters must be passed to'
    
def test_if_parameters_are_not_int_and_raise_exception():
    response = client.post('/sum/?a=4&b=abc')
    assert response.status_code == 422