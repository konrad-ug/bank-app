import unittest

from ..KontoJunior import KontoJunior

class TestKontoJunior(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    imie_opiekuna= "Anna"
    nazwisko_opiekuna = "Januszewska"
    pesel_opiekuna = "12345678901"
    limit = 1000


   
    def test_zakladanie_konta(self):
        konto = KontoJunior(self.imie, self.nazwisko, self.pesel, self.imie_opiekuna, self.nazwisko_opiekuna, self.pesel_opiekuna, self.limit)
        self.assertEqual(konto.saldo, 0)
        self.assertEqual(konto.imie, self.imie)
        self.assertEqual(konto.nazwisko, self.nazwisko)
        self.assertEqual(konto.pesel, self.pesel)
        self.assertEqual(konto.imie_opiekuna, self.imie_opiekuna)
        self.assertEqual(konto.nazwisko_opiekuna, self.nazwisko_opiekuna)
        self.assertEqual(konto.pesel_opiekuna, self.pesel_opiekuna)
        self.assertEqual(konto.historia, [])
        self.assertEqual(konto.limit, self.limit)

    def test_przelew_wiekszy_niz_limit(self):
        konto = KontoJunior(self.imie, self.nazwisko, self.pesel, self.imie_opiekuna, self.nazwisko_opiekuna, self.pesel_opiekuna, self.limit)
        konto.saldo = 5000
        konto.przelew(1001)
        self.assertEqual(konto.saldo, 5000)
        self.assertListEqual(konto.historia, [])

    def test_przelew_mniejszy_niz_limit(self):
        konto = KontoJunior(self.imie, self.nazwisko, self.pesel, self.imie_opiekuna, self.nazwisko_opiekuna, self.pesel_opiekuna, self.limit)
        konto.saldo = 5000
        konto.przelew(500)
        self.assertEqual(konto.saldo, 4500)
        self.assertListEqual(konto.historia, [-500])

    def test_przelew_rowny_limitowi(self):
        konto = KontoJunior(self.imie, self.nazwisko, self.pesel, self.imie_opiekuna, self.nazwisko_opiekuna, self.pesel_opiekuna, self.limit)
        konto.saldo = 5000
        konto.przelew(1000)
        self.assertEqual(konto.saldo, 4000)
        self.assertListEqual(konto.historia, [-1000])

    def test_zakladanie_konta_bez_podania_opiekuna(self):
        self.assertRaises(ValueError, KontoJunior, self.imie, self.nazwisko, self.pesel, None, None, None, self.limit)
        

