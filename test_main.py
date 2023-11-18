from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch #helps store api
from user_service import UserService

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id":1, "name":"Item One", "description":"This is item one"}

mock_users = [
    {"username":"Ade"},
    {"username":"Bola"}
]
#Mock the UserService Class
def  test_get_users_from_db():
    with patch("main.user_service", spec=UserService) as mock_user_service:
        mock_user_service.get_users_from_db.return_value = mock_users
        response = client.get("/users")
        assert response.status_code == 200
        assert response.json() == mock_users

        #Assert that the get_users_from_db method was called once
        mock_user_service.get_users_from_db.assert_called_once()