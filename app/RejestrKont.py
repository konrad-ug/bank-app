from app.Konto import Konto

class RejestrKont():
    lista = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista.append(konto)

    @classmethod    
    def ile_kont(cls):
        return len(cls.lista)
    
    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                return konto

    @classmethod
    def usun_konto_z_peselem(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                cls.lista.remove(konto)
        return True

    @classmethod
    def wyczysc_rejestr(cls):
        cls.lista = []
        return cls.lista
