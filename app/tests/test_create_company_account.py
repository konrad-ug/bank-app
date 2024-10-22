import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz sp. z o.o."
    nip = "1234567890"
    
    def test_tworzenie_konta(self):
        pierwsze_konto = CompanyAccount(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Nazwa nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_za_krotki_nip(self):
        krotki_nip = "123"
        konto = CompanyAccount(self.name, krotki_nip)
        self.assertEqual(konto.nip, "Niepoprawny nip!", "nip nie został zapisany!")

    def test_za_dlugi_nip(self):
        nip = "1232353453453453453"
        konto = CompanyAccount(self.name, nip)
        self.assertEqual(konto.nip, "Niepoprawny nip!", "Nip nie został zapisany!")
