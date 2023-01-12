import datetime
from app.Kantor import Kantor

class Konto:
    oplata_za_przelew_ekspresowy = 1
    def __init__(self, imie, nazwisko, pesel, kod_promocyjny = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.historia = []
        self.pesel = pesel if self.czy_poprawny_pesel(pesel) else "Nieporpwany pesel!"
        if self.czy_promocja_dziala(pesel, kod_promocyjny):
            self.saldo = 50
        else:
            self.saldo = 0

    def czy_poprawny_pesel(self, pesel):
        return len(pesel) == 11

    def czy_promocja_dziala(self, pesel, kod_promocyjny):
        return self.czy_dobry_kod_promocyjny(kod_promocyjny) and self.czy_urodzony_po_65(pesel)

    def czy_urodzony_po_65(self, pesel):
        rok_urodzenia = int(pesel[0:2])
        miesiac_urodzenia = int(pesel[2:4])
        if miesiac_urodzenia > 20: #osoby urodzone po 2000 roku
            return True
        return rok_urodzenia > 65

    def czy_dobry_kod_promocyjny(self, kod_promocyjny):
        if kod_promocyjny != None:
            if kod_promocyjny[0:5] == "PROM_" and len(kod_promocyjny) == 8:
                return True
        return False

    def zaksieguj_przelew_przychodzacy(self, kwota: int):
        self.saldo += kwota
        self.historia.append(kwota)

    def zaksieguj_przelew_wychodzacy(self, kwota: int):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.historia.append(-kwota)

    def zaksieguj_przelew_ekspresowy(self, kwota: int):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.historia.append(-kwota)
            self.saldo -= self.oplata_za_przelew_ekspresowy
            self.historia.append(-self.oplata_za_przelew_ekspresowy)

    def zaksieguj_przelew_przychodzacy_walutowy(self, kwota, waluta):
        kurs = self.pobierz_kurs_pary_walutowej(waluta, "PLN")
        kwota_w_pln = kwota * kurs
        self.saldo += kwota_w_pln
        self.historia.append(kwota_w_pln) 

    def zaciagnij_kredyt(self, kwota):
        if len(self.historia) < 3:
            return False
        if self.historia[-3] > 0 and self.historia[-2] > 0 and self.historia[-1] > 0:
            self.saldo += kwota
            return True
        if len(self.historia) < 5:
            return False
        if sum(self.historia[-5:]) <= kwota:
            return False
        self.saldo += kwota
        return True

    def wyslij_historie_na_maila(self, adresat, smtp_connection):
        tresc = f"Twoja historia konta to: {self.historia}"
        temat = f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}"
        return smtp_connection.wyslij(temat, tresc, adresat)
