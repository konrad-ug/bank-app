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
        ("test_empty_history", [], 1000, 0),
        ("3 positive transactions", [-4, -1000, 100, 200, 300], 1000, 1000),
        ("test_sum_higher_than_loan", [-4, 5000, -100, 200, -300], 1000, 1000)
    ])
    def test_loan(self, name, history, loan, expected):
        print(f"Test: {name}")
        self.konto.history = history
        self.konto.take_loan(loan)
        self.assertEqual(self.konto.saldo, expected, "Saldo nie zostało zwiększone")

    # def test_empty_history(self):
    #     self.konto.history = []
    #     self.konto.take_loan(1000)
    #     self.assertEqual(self.konto.saldo, 0, "Saldo zostało zwiększone!")

    # def test_3_positive_transactions(self):
    #     self.konto.history = [-4, -1000, 100, 200, 300]
    #     self.konto.take_loan(1000)
    #     self.assertEqual(self.konto.saldo, 1000, "Saldo zostało zwiększone!")

    # def test_sum_higher_than_loan(self):
    #     self. konto.history = [-4, 5000, -100, 200, -300]
    #     self.konto.take_loan(1000)
    #     self.assertEqual(self.konto.saldo, 1000, "Saldo zostało zwiększone!")
















    # def test_empty_history(self):
    #     self.konto.take_loan(1000)
    #     self.assertEqual(self.konto.saldo, 0, "Saldo zostało zwiększone!")

    # def test_3_positive_transactions(self):
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-4, -1000, 100, 200, 300]
    #     konto.take_loan(1000)
    #     self.assertEqual(konto.saldo, 1000, "Saldo zostało zwiększone!")

    # def test_2_positive_transactions(self):
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-4, -1000, -100, 200, 300]
    #     konto.take_loan(1000)
    #     self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    # def test_sum_higher_than_loan(self):
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-4, 5000, -100, 200, -300]
    #     konto.take_loan(1000)
    #     self.assertEqual(konto.saldo, 1000, "Saldo zostało zwiększone!")

    # def test_sum_lower_than_loan(self):
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [-4, 5000, -100, 200, -300]
    #     konto.take_loan(20000)
    #     self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")

    # def test_single_transaction(self):
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = [5000]
    #     konto.take_loan(1000)
    #     self.assertEqual(konto.saldo, 0, "Saldo zostało zwiększone!")




    # def setUp(self):
    #     self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ("test_empty_history", [], 1000, 0),
        ("3 positive transactions", [-4, -1000, 100, 200, 300], 1000, 1000),
    ])
    def test_loan(self, name, history, loan, expected):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = history
        konto.take_loan(loan)
        self.assertEqual(konto.saldo, expected, "Saldo nie zostało zwiększone!")















    # def setUp(self):
    #     self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)

    # @parameterized.expand([
    #     ([-100, 200, -33, 10, 200, 50], 1000, 1000),
    #     ([-100, 200, 5000, 1, -2, -3], 1000, 1000),
    #     ([-100, 200, 5000, 1, -2, -3], 1000, 1000),
    #     ([-100, 200, 500, 100, -1, 300], 10000, 0),
    #     ([200, 500], 10000, 0),
    #     ([-666, 200000, 500, -1, 200], 10000, 10000)
    # ])
    # def test_loan(self, history, loan, expected):
    #     self.konto.history = history
    #     self.konto.take_loan(loan)
    #     self.assertEqual(self.konto.saldo, expected, "Saldo nie zostało zwiększone!")