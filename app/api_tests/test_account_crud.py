import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    url = "http://127.0.0.1:5000/api/accounts"
    payload = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "12345678901"
    }
    
    def test_create_account(self):
        response = requests.post(self.url, json=self.payload)
        assert response.status_code == 201
        assert response.json()["message"] == "Account created"

    def test_get_account_by_pesel(self):
        response = requests.get(f"{self.url}/{self.payload['pesel']}")
        assert response.status_code == 200
        assert response.json()["name"] == self.payload['name']
        assert response.json()["surname"] == self.payload['surname']
        assert response.json()["saldo"] == 0

    def test_none_existing_account(self):
        response = requests.get(f"{self.url}/12345678902")
        assert response.status_code == 404
    