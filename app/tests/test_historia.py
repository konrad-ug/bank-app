import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from ..SMTPConnection import SMTPConnection
from unittest.mock import patch
from unittest.mock import MagicMock
from datetime import datetime

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

    def test_wysyłanie_maila_z_historia(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_maila("konrad@gmail.com", smtp_connector)
        self.assertTrue(status)
        status = konto.wyslij_historie_na_maila("konrad@gmail.com", smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "konrad@gmail.com")

    def test_wysyłanie_maila_z_historia_niepowodzenie(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = False)
        status = konto.wyslij_historie_na_maila("konrad@gmail.com", smtp_connector)
        self.assertFalse(status)

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje_w_gov')
    def test_mail_z_historia_konto_firmowe(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_maila("firmowe@gmail.com", smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Historia konta Twojej firmy to: {konto.historia}", "firmowe@gmail.com")
