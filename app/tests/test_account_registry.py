import unittest

from ..PersonalAccount import PersonalAccount
from ..AccountRegistry import AccountRegistry

class TestRegistry(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    pesel_66 = "12345678966"
    pesel_77 = "12345678977"

    @classmethod
    def setUpClass(cls):
        cls.konto = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel)
        cls.konto2 = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel_66)
        cls.konto3 = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel_77)

    def setUp(self):
        AccountRegistry.accounts = []
        AccountRegistry.add_account(self.konto)

    def test_add_account_to_registry(self):
        AccountRegistry.add_account(self.konto2)
        self.assertEqual(AccountRegistry.get_account_count(), 2)
    
    def test_add_multiple_accounts_to_registry(self):
        AccountRegistry.add_account(self.konto)
        AccountRegistry.add_account(self.konto2)
        AccountRegistry.add_account(self.konto3)
        self.assertEqual(AccountRegistry.get_account_count(), 4)

    def test_get_account_by_pesel(self):
        AccountRegistry.add_account(self.konto)
        AccountRegistry.add_account(self.konto2)
        AccountRegistry.add_account(self.konto3)
        self.assertEqual(AccountRegistry.get_account_by_pesel(self.pesel_66), self.konto2)
        self.assertEqual(AccountRegistry.get_account_by_pesel(self.pesel_77), self.konto3)

   
