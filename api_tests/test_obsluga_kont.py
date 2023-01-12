import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "nick",
        "nazwisko": "cave",
        "pesel": "01292909876"
    }

    # odpalanie flaska
    # export FLASK_APP=app/api.py
    # python3 -m flask run
    # odpalanie testu
    # python3 -m unittest api_tests/test_obsluga_kont.py

    url = "http://localhost:5000"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json = self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_get_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_3_usuniecie_konta(self):
        delete_response = requests.delete(self.url + "/konta/konto/" + self.body['pesel'])
        self.assertEqual(delete_response.status_code, 202)