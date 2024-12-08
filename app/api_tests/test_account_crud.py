import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    url = "http://127.0.0.1:5002/api/accounts"
    payload = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "12345678901"
    }

    def setUp(self):
        response = requests.post(self.url, json=self.payload)
        self.assertEqual(response.status_code, 201)

    def tearDown(self) -> None:
        response = requests.delete(f"{self.url}/{self.payload['pesel']}")
        self.assertEqual(response.status_code, 200)

    def test_creating_account_wit_the_same_pesel(self):
        response = requests.post(self.url, json=self.payload)
        self.assertEqual(response.status_code, 409)

    def test_get_account_by_pesel(self):
        response = requests.get(f"{self.url}/{self.payload['pesel']}")
        assert response.status_code == 200
        assert response.json()["name"] == self.payload['name']
        assert response.json()["surname"] == self.payload['surname']
        assert response.json()["saldo"] == 0

    def test_none_existing_account(self):
        response = requests.get(f"{self.url}/12345678902")
        assert response.status_code == 404
    