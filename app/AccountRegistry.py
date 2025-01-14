from app.PersonalAccount import PersonalAccount

class AccountRegistry:
    accounts = []

    @classmethod
    def add_account(cls, account):
        cls.accounts.append(account)

    @classmethod
    def get_account_count(cls):
        return len(cls.accounts)
    
    @classmethod
    def get_account_by_pesel(cls, pesel) -> PersonalAccount:
        for account in cls.accounts:
            if account.pesel == pesel:
                return account
        return None