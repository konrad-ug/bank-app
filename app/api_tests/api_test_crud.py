import unittest
import requests

class TestAPI_CRUD(unittest.TestCase):
    body = {
        "name" : "Dariusz",
        "surname": "Januszewski",
        "pesel":"12345678901"
    }
    url = "http://localhost:5000/api/accounts"
    
    def test_create_account(self):
        response = requests.post(self.url, json=self.body)
        self.assertEqual(response.status_code, 201, "Wrong status code!")

    def test_search_by_pesel_none_existing(self):
        response = requests.post(self.url, json=self.body)
        response_search = requests.get(f"{self.url}/12345678901")
        self.assertEqual(response_search.status_code, 200)