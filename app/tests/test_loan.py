import unittest

from ..PersonalAccount import PersonalAccount

class TestLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"


    def test_loan_3_last_incoming_transfers(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = [-4, 222, 100, 555]
        konto.take_loan(1000)
        self.assertEqual(konto.saldo, 1000)

    def test_loan_empty_history(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = []
        konto.take_loan(1000)
        self.assertEqual(konto.saldo, 0)

   
