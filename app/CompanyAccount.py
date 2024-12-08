from .Konto import Konto
import os
import datetime
import requests


class CompanyAccount(Konto):
    express_transfer_fee = 5

    def __init__(self, name, nip):
        self.name = name
        if len(nip) != 10:
            self.nip = "Niepoprawny nip!"
        elif self.is_nip_valid(nip):
            self.nip = nip
        else:
            raise ValueError("Niepoprawny nip!")

    @classmethod
    def is_nip_valid(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        nip_path = f"{gov_url}api/search/nip/{nip}/?date={today}"
        print(f"sending requests to {nip_path}")
        response = requests.get(nip_path)
        print(f"Response dla nipu: {response.status_code}, {response.json()}")
        if response.status_code == 200:
            return True
        return False
