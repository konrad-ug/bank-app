import datetime

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
