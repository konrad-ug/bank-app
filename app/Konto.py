class Konto:
    saldo = 0
    express_transfer_fee = 2
    history = []

    def incoming_transfer(self, kwota):
        self.saldo += kwota
        self.history.append(kwota)

    def outgoing_transfer(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.history.append(kwota)

    def outgoing_express_transfer(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota + self.express_transfer_fee
            self.history.append(kwota)
            self.history.append(-self.express_transfer_fee)

