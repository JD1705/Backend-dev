from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)
    
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