from .Konto import Konto

class CompanyAccount(Konto):
    express_transfer_fee = 5
    
    def __init__(self, name, nip):
        self.name = name
        if len(nip) == 10:
            self.nip = nip
        else:
            self.nip = "Niepoprawny nip!"
        self.saldo = 0

