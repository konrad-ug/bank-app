import unittest
from parameterized import parameterized

from ..Konto import Konto

class TestKredytRefaktor(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([100, 100, 100], 500, True, 500),
        ([-100, 100, -100, 100, 1000], 700, True, 700),
        ([-100, 20000, -100, 100, -1000], 1000, True, 1000),
        ([100], 666, False, 0),
        ([-100, 100, 100, 100, -600, 200], 500, False , 0),
    ])
    def test_zaciaganie_kredytu(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)
    



    
    # def test_3_mieszane_przelewy(self):
    #     self.konto.historia = [-100, 100, -100, 100]
    #     czy_przyznany = self.konto.zaciagnij_kredyt(500)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, 0)

    # def test_5_przelewow_kwota_wieksza(self):
    #     self.konto.historia = [-100, 100, -100, 100, 1000]
    #     czy_przyznany = self.konto.zaciagnij_kredyt(700)
    #     self.assertTrue(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, 700)

    # def test_5_przelewow_kwota_mniejsza(self):
    #     self.konto.historia = [-100, 100, -100, 100, 200]
    #     czy_przyznany = self.konto.zaciagnij_kredyt(700)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, 0)

    # def test_2_przychodzace_przelewy(self):
    #     self.konto.historia = [100, 1000]
    #     czy_przyznany = self.konto.zaciagnij_kredyt(500)
    #     self.assertFalse(czy_przyznany)
    #     self.assertEqual(self.konto.saldo, 0)
