import unittest
from unittest.mock import patch

from ..KontoFirmowe import KontoFirmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje_w_gov')
    def test_tworzenie_konta(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = False
        pierwsze_konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        self.assertIsNone(pierwsze_konto)
        self.assertEqual(pierwsze_konto.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie została zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP nie zostało zapisany!")

    def test_zbyt_dlugi_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "84616275639887")
        self.assertEqual(konto.nip, "Nieporpwany NIP!")

    def test_zbyt_krotki_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "846162")
        self.assertEqual(konto.nip, "Nieporpwany NIP!")

    def test_czy_nip_istnieje_w_gov(self):
        pass


    

