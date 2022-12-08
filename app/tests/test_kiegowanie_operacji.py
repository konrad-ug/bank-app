import unittest
from unittest.mock import patch

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowaniePrzelewow(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "61092909876"

    def test_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 100)

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 105
        konto.zaksieguj_przelew_wychodzacy(100) 
        self.assertEqual(konto.saldo, 5)

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 80
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 80)

    def test_seria_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(250) #saldo po operacji 750
        konto.zaksieguj_przelew_przychodzacy(10.25) 
        self.assertEqual(konto.saldo, 760.25)

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje_w_gov')
    def test_seria_przelewow_konto_firmowe(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True
        konto = KontoFirmowe("Kebabex", "8461627563")
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(250) #saldo po operacji 750
        konto.zaksieguj_przelew_wychodzacy(1500) #saldo po operacji 750
        konto.zaksieguj_przelew_przychodzacy(10.25) 
        self.assertEqual(konto.saldo, 760.25)

    

