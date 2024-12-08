class Konto:
    saldo = 0
    express_transfer_fee = 0
    
    def incoming_transfer(self, kwota):
        self.saldo += kwota
        return True

    def outgoing_transfer(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            return True
        return False

    def outgoing_express_transfer(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota + self.express_transfer_fee
            return True
        return False