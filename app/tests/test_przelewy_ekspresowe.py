import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowaniePrzelewow(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "61092909876"

    def test_udany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 1000 - 300 -1)

    def test_nieudany_przelew_ekpresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 200
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 200)

    def test_udany_przelew_ekspresowy_konto_firmowe(self):
        konto = KontoFirmowe("Kebabex ltd.", "8461627563")
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 1000 -300 -5)

    def test_udany_przelew_ekpresowy_saldo_ponizej_0(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 200
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, -1)

    

