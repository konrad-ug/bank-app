import unittest

from ..Konto import Konto

class TestKredyt(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"

    def test_3_przychodzace_przelewy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, 100, 100]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 500)
    
    def test_3_mieszane_przelewy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, -100, 100]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)

    def test_5_przelewow_kwota_wieksza(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, -100, 100, 1000]
        czy_przyznany = konto.zaciagnij_kredyt(700)
        self.assertTrue(czy_przyznany)
        self.assertEqual(konto.saldo, 700)

    def test_5_przelewow_kwota_mniejsza(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, -100, 100, 200]
        czy_przyznany = konto.zaciagnij_kredyt(700)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)

    def test_2_przychodzace_przelewy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [100, 1000]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(konto.saldo, 0)
