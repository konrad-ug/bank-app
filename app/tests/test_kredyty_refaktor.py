import unittest

from ..Konto import Konto

class TestKredytRefaktor(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    def test_3_przychodzace_przelewy(self):
        self.konto.historia = [-100, 100, 100, 100]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(self.konto.saldo, 500)
    
    def test_3_mieszane_przelewy(self):
        self.konto.historia = [-100, 100, -100, 100]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(self.konto.saldo, 0)

    def test_5_przelewow_kwota_wieksza(self):
        self.konto.historia = [-100, 100, -100, 100, 1000]
        czy_przyznany = self.konto.zaciagnij_kredyt(700)
        self.assertTrue(czy_przyznany)
        self.assertEqual(self.konto.saldo, 700)

    def test_5_przelewow_kwota_mniejsza(self):
        self.konto.historia = [-100, 100, -100, 100, 200]
        czy_przyznany = self.konto.zaciagnij_kredyt(700)
        self.assertFalse(czy_przyznany)
        self.assertEqual(self.konto.saldo, 0)

    def test_2_przychodzace_przelewy(self):
        self.konto.historia = [100, 1000]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(self.konto.saldo, 0)
