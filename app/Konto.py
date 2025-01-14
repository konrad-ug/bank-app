import datetime
from app.SMTPClient import SMTPClient
class Konto:
    saldo = 0
    express_transfer_fee = 0
    history = []
    email_text = "Twoja historia konta to: " + str(history)
    
    def incoming_transfer(self, kwota):
        self.saldo += kwota
        self.history.append(kwota)
        return True

    def outgoing_transfer(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.history.append(-kwota)
            return True
        return False

    def outgoing_express_transfer(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota + self.express_transfer_fee
            self.history.append(-kwota)
            self.history.append(-self.express_transfer_fee)
            return True
        return False
    
    def send_history_to_email(self, email):
        subject = "Wyciąg z dnia " + datetime.datetime.now().strftime('%Y-%m-%d')
        text = self.email_text + str(self.history)
        # return smtp_client.send(subject, text, email)

