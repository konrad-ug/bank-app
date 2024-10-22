import unittest

from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    name = "Dariusz sp. z o.o."
    nip = "1234567890"

    def test_incoming_transfer(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.incoming_transfer(100)
        self.assertEqual(konto.saldo, 100, "Saldo nie zostało zwiększone!")

    def test_outgoing_transfer(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 110
        konto.outgoing_transfer(50)
        self.assertEqual(konto.saldo, 60, "Saldo nie zostało zmniejszone!")

    def test_outgoing_transfer_too_much(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 110
        konto.outgoing_transfer(150)
        self.assertEqual(konto.saldo, 110, "Saldo nie zostało zmniejszone!")

    def test_transfers(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.incoming_transfer(100)
        konto.outgoing_transfer(50)
        konto.incoming_transfer(1000)
        self.assertEqual(konto.saldo, 1050, "Saldo nie zostało poprawnie zmnienione!")

    def test_incoming_company_transfer(self):
        konto = CompanyAccount(self.name, self.nip)
        konto.incoming_transfer(100)
        self.assertEqual(konto.saldo, 100, "Saldo nie zostało zwiększone!")

    def test_outgoing_company_transfer(self):
        konto = CompanyAccount(self.name, self.nip)
        konto.saldo = 110
        konto.outgoing_transfer(50)
        self.assertEqual(konto.saldo, 60, "Saldo nie zostało zmniejszone!")

    def test_outgoing_company_transfer_too_much(self):
        konto = CompanyAccount(self.name, self.nip)
        konto.saldo = 110
        konto.outgoing_transfer(150)
        self.assertEqual(konto.saldo, 110, "Saldo nie zostało zmniejszone!")

    def test_outgoing_company_express_transfer(self):
        konto = CompanyAccount(self.name, self.nip)
        konto.saldo = 110
        konto.outgoing_express_transfer(50)
        self.assertEqual(konto.saldo, 110-50-5, "Opłata nie została naliczona!")

    def test_outgoing_express_personal_transfer(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 110
        konto.outgoing_express_transfer(50)
        self.assertEqual(konto.saldo, 110-50-1, "Opłata nie została naliczona!")

    def test_outgoing_express_transfer_too_much(self):
        konto = CompanyAccount(self.name, self.nip)
        konto.saldo = 110
        konto.outgoing_express_transfer(150)
        self.assertEqual(konto.saldo, 110, "Saldo nie zostało zmniejszone!")

   