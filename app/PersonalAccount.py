from .Konto import Konto

class PersonalAccount(Konto):
    express_transfer_fee = 1

    def __init__(self, imie, nazwisko, pesel, kod_promocyjny=None):
        self.imie = imie
        self.nazwisko = nazwisko
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
        if self.czy_kod_poprawny(kod_promocyjny):
            self.saldo = 50
        else:
            self.saldo = 0

    def czy_kod_poprawny(self, kod_promocyjny):
        if kod_promocyjny is None:
            return False
        if kod_promocyjny.startswith("PROM_") and len(kod_promocyjny) == 8:
            return True
        return False
    
    

    
 
    