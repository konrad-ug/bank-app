from app.Konto import Konto
import requests
import os
import datetime
class KontoFirmowe(Konto):
    oplata_za_przelew_ekspresowy = 5

    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.historia = []
        self.nip = nip if self.czy_poprawny_nip(nip) else "Nieporpwany NIP!"
        if not self.czy_nip_istnieje_w_gov(nip):
            return None

    def czy_poprawny_nip(self, nip):
        return len(nip) == 10

    @classmethod
    def czy_nip_istnieje_w_gov(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        nip_path = f"{gov_url}api/search/nip/{nip}/?date={today}"
        print(f"sending requests to {nip_path}")
        response = requests.get(nip_path)
        print(f"Response dla nipu: {response.status_code}, {response.json()}")
        if response.status_code == 200:
            return True
        return False

    def wyslij_historie_na_maila(self, adresat, smtp_connection):
        tresc = f"Historia konta Twojej firmy to: {self.historia}"
        temat = f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}"
        return smtp_connection.wyslij(temat, tresc, adresat)