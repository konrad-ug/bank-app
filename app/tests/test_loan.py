import unittest

from ..PersonalAccount import PersonalAccount

class TestLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"

    def test_loan_3_last_incoming(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = [-100, 200, -33, 10, 200, 50]
        konto.take_loan(1000)
        self.assertEqual(konto.saldo, 1000, "Saldo nie zostało zwiększone!")

    def test_loan_5_transactions(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = [-100, 200, 5000, 1, -2, -3]
        konto.take_loan(1000)
        self.assertEqual(konto.saldo, 1000, "Saldo nie zostało zwiększone!")

    def test_loan_negative(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = [-100, 200, 500, 100, -1, 300]
        konto.take_loan(10000)
        self.assertEqual(konto.saldo, 0, "Saldo nie zostało zwiększone!")

    def test_loan_2_positions_in_history(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = [200, 500]
        konto.take_loan(10000)
        self.assertEqual(konto.saldo, 0, "Saldo nie zostało zwiększone!")
    
    def test_loan_2_positions_in_history_high_sum(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = [-666, 200000, 500, -1, 200]
        konto.take_loan(10000)
        self.assertEqual(konto.saldo, 10000, "Saldo nie zostało zwiększone!")