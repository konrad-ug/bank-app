import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie zostało zapisany!")

    def test_zbyt_dlugi_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "890786756545342324354")
        self.assertEqual(konto.pesel, "Nieporpwany pesel!")

    def test_zbyt_krotki_pesel(self):
        konto = Konto(self.imie, self.nazwisko, "890786")
        self.assertEqual(konto.pesel, "Nieporpwany pesel!")

    def test_poprawny_kod_promocyjny(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_123")
        self.assertEqual(konto.saldo, 50)

    def test_zly_poczatek_kodu_promocyjnego(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "zly_123")
        self.assertEqual(konto.saldo, 0)

    def test_zbyt_dlugi_kod_promocyjny(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_1234")
        self.assertEqual(konto.saldo, 0)

    def test_osoba_urodzona_przed_65(self):
        konto = Konto(self.imie, self.nazwisko, "61092909876", "PROM_123")
        self.assertEqual(konto.saldo, 0)

    def test_osoba_urodzona_po_2000(self):
        konto = Konto(self.imie, self.nazwisko, "01292909876", "PROM_123")
        self.assertEqual(konto.saldo, 50)  


