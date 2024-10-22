import unittest

from ..PersonalAccount import PersonalAccount

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    
    def test_tworzenie_konta(self):
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "PESEL nie został zapisany!")

    def test_za_krotki_pesel(self):
        krotki_pesel = "123"
        konto = PersonalAccount(self.imie, self.nazwisko, krotki_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!")

    def test_za_dlugi_pesel(self):
        krotki_pesel = "1232353453453453453"
        konto = PersonalAccount(self.imie, self.nazwisko, krotki_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!")

    def test_zly_kod_suffix(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel, "PROM_d23r3r3s")
        self.assertEqual(konto.saldo, 0, "Pesel nie został zapisany!")

    def test_zly_kod_preffix(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel, "PRO_123")
        self.assertEqual(konto.saldo, 0, "Pesel nie został zapisany!")

def test_dobry_kod(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel, "PROM_123")
        self.assertEqual(konto.saldo, 50, "Pesel nie został zapisany!")