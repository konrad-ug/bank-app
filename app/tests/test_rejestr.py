import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestr(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"

    @classmethod
    def setUpClass(cls):
        konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_1_dodawanie_pierwszego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto1 = Konto(self.imie + "ddd", self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        RejestrKont.dodaj_konto(konto1)
        self.assertEqual(RejestrKont.ile_kont(), 3)

    def test_2_dodawania_drugie_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 4)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []