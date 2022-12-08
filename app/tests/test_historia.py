import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

class TestCreateBankAccount(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def test_zapisywanie_przelewu_przychodzaceo(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertListEqual(konto.historia, [100])

    def test_zapisywanie_przelewu_wychodzacego(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertListEqual(konto.historia, [-100])

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje_w_gov')
    def test_zapisywanie_przelewu_wkspresowego_konto_firmowe(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(100)
        self.assertListEqual(konto.historia, [-100, -5])

    def test_zapisywanie_przelewu_wkspresowego(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 888
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertListEqual(konto.historia, [-300, -1])
