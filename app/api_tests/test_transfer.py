import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    url = "http://127.0.0.1:5002/api/accounts"
    payload = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "12345678901"
    }
    pesel = payload['pesel']

    def setUp(self):
        response = requests.post(self.url, json=self.payload)
        self.assertEqual(response.status_code, 201)

    def tearDown(self) -> None:
        response = requests.delete(f"{self.url}/{self.payload['pesel']}")
        self.assertEqual(response.status_code, 200)

    def test_succes_incoming_transfer(self):
        response = requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "incoming", "amount": 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Incoming transfer processed")
        konto_response = requests.get(f"{self.url}/{self.pesel}")
        self.assertEqual(konto_response.json()["saldo"], 100)

    def test_success_outgoing_transfer(self):
        requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "incoming", "amount": 100})
        response = requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "outgoing", "amount": 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Outgoing transfer processed")
        konto_response = requests.get(f"{self.url}/{self.pesel}")
        self.assertEqual(konto_response.json()["saldo"], 0)

    def test_failed_outgoing_transfer(self):
        response = requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "outgoing", "amount": 1000})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"], "Transfer failed")

    def test_failed_express_transfer(self):
        response = requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "express", "amount": 100})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"], "Transfer failed")

    def test_success_express_transfer(self):
        requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "incoming", "amount": 100})
        response = requests.post(f"{self.url}/{self.pesel}/transfer", json={"type": "express", "amount": 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Outgoing transfer processed")
        konto_response = requests.get(f"{self.url}/{self.pesel}")
        self.assertEqual(konto_response.json()["saldo"], 100-100-1)
    