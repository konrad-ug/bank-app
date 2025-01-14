import unittest
from unittest.mock import MagicMock, patch
import datetime

from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount
from ..SMTPClient import SMTPClient

class TestSendHistoryToEmail(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    name = "Dariusz sp. z o.o."
    nip = "1234567890"
    SMTPClient.send = MagicMock(return_value=True)
    
    expected_history = [100, 50, 1000]
    expected_email_text = f"Twoja historia konta to: {expected_history}"
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    expected_email_subject = f"Wyciąg z dnia {today}"
    email = "januszewski@ug.edu.pl"
   
       
    def test_example_magick_mock(self):
        smtp_client = SMTPClient()
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.history = self.expected_history
        result = konto.send_history_to_email(self.email, smtp_client)
        self.assertTrue(result)
        # smtp_client.send.assert_called_once()
        # smtp_client.send.assert_called_with(self.expected_email_subject, self.expected_email_text, self.email)
        
        
       
       
       
       

    # def test_send_history_to_email(self):
    #     smtp_client = SMTPClient()
    #     smtp_client.send = MagicMock(return_value=True)
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = self.expected_history
    #     result = konto.send_history_to_email(self.email)
    #     self.assertTrue(result)
    #     smtp_client.send.assert_called_once()
    #     smtp_client.send.assert_called_with(self.expected_email_subject, self.expected_email_text, self.email)
        
    
    
    
    
    # @patch("app.SMTPClient.SMTPClient.send")
    # def test_with_patch(self, mock_send):
    #     smtp_client = SMTPClient()
    #     mock_send.return_value = True
        
    #     konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.history = self.expected_history
    #     result = konto.send_history_to_email(self.email, smtp_client)
    #     self.assertTrue(result)
        
    #     args, kwargs = mock_send.call_args
    #     self.assertEqual(args[0], self.expected_email_subject)
    #     self.assertEqual(args[1], self.expected_email_text)
    #     self.assertEqual(args[2], self.email)
        
        


        
        


   