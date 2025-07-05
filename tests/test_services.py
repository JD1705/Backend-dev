import pytest
from ..app.schemas.user_schema import UserInModel
from ..app.services.service import create_user_logic, HTTPException, search_user_email

# mock tests for create user service
def test_create_user_logic(mocker):
    mock_db = mocker.MagicMock()
    mock_db.__getitem__.return_value.find_one.return_value = False
    mock_db.__getitem__.return_value.insert_one.return_value.inserted_id = "507f1f77bcf86cd799439011"
    
    test_data = UserInModel(
        username="JD",
        email="test@test.com",
        password="12345",
        first_name="John",
        last_name="Doe"
    )
    result = create_user_logic(test_data, mock_db)
    
    assert result == {
        'message': 'User created successfully',
        'status_code': 201,
        'insertion_id': "507f1f77bcf86cd799439011"
    }
    
def test_user_already_exist(mocker):
    mock_db = mocker.MagicMock()
    mock_db.__getitem__.return_value.find_one.return_value = True
    
    test_data = UserInModel(
        username="JD",
        email="test@test.com",
        password="12345",
        first_name="John",
        last_name="Doe"
    )
    
    with pytest.raises(HTTPException) as error_info:
        create_user_logic(test_data,mock_db)
    
    assert error_info.value.status_code == 409
    assert 'User email already registered. Try another one' in str(error_info.value.detail)
    

# mock test for search user by email
def test_search_user_in_db_by_email(mocker):
    mock_db = mocker.MagicMock()
    mock_db.__getitem__.return_value.find_one.return_value = {
        "username":'test_name',
        "email":"test@test.com",
        "first_name":"test",
        "last_name":"name"
    }
    
    test_email = 'test@test.com'
    
    result = search_user_email(test_email,mock_db)
    
    assert result == {
        "username":'test_name',
        "email":"test@test.com",
        "first_name":"test",
        "last_name":"name"
    }
    
    
def test_user_email_not_found(mocker):
    mock_db = mocker.MagicMock()
    mock_db.__getitem__.return_value.find_one.return_value = False
    
    test_email = 'test@test.com'
    
    with pytest.raises(HTTPException) as error_info:
        search_user_email(test_email,mock_db)
    
    assert error_info.value.status_code == 404
    assert 'User Not Found' in str(error_info.value.detail)