import unittest

from ..PersonalAccount import PersonalAccount
from parameterized import parameterized

class TestLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"


    def setUp(self):
        self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([100, 100, 100], 500, True, 500),
        ([-100, 100, -100, 100, 1000], 700, True, 700),
        ([-100, 20000, -100, 100, -1000], 1000, True, 1000),
        ([100], 666, False, 0),
        ([-100, 100, 100, 100, -600, 200], 500, False , 0),
    ])
    def test_zaciaganie_kredytu(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.history = historia
        czy_przyznany = self.konto.take_loan(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

   
