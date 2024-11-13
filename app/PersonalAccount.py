from .Konto import Konto

class PersonalAccount(Konto):
    express_transfer_fee = 1
    history = []

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
    
    def take_loan(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            return True
        return False
    
    def take_loan(self, kwota):
        if len(self.history) < 3:
            return False
        if self.history[-3] > 0 and self.historia[-2] > 0 and self.historia[-1] > 0:
            self.saldo += kwota
            return True
        if len(self.historia) < 5:
            return False
        if sum(self.historia[-5:]) <= kwota:
            return False
        self.saldo += kwota
        return True

    # def zaciagnij_kredyt(self, kwota):
    #     if self.czy_ostatnie_n_transakcji_byly_wplatami(3) or self.oblicz_sume_ostatnich_n_transakcji(5) > kwota: 
    #         self.saldo += kwota
    #         return True
    #     return False
        
    # def czy_ostatnie_n_transakcji_byly_wplatami(self, n):
    #     if len(self.historia) < n:
    #         return False
    #     for ksiegowanie in self.historia[-n:]:
    #         if ksiegowanie < 0:
    #             return False
    #     return True

    # def oblicz_sume_ostatnich_n_transakcji(self, n):
    #     if len(self.historia) < n:
    #         return False
    #     return sum(self.historia[-n:])
    

    
 
    