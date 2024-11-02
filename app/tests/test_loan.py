import unittest
from parameterized import parameterized

from ..PersonalAccount import PersonalAccount

class TestLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"

    def setUp(self) -> None:
        self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100, 200, -33, 10, 200, 50], 1000, 1000),
        ([-100, 200, 5000, 1, -2, -3], 1000, 1000),
        ([-100, 200, 5000, 1, -2, -3], 1000, 1000),
        ([-100, 200, 500, 100, -1, 300], 10000, 0),
        ([200, 500], 10000, 0),
        ([-666, 200000, 500, -1, 200], 10000, 10000)
    ])
    def test_loan(self, history, loan, expected):
        print(f"Test dla historii: {history}, pożyczki: {loan}, oczekiwane saldo: {expected}")
        self.konto.history = history
        self.konto.take_loan(loan)
        self.assertEqual(self.konto.saldo, expected, "Saldo nie zostało zwiększone!")