import unittest

from source import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_create_account(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski")