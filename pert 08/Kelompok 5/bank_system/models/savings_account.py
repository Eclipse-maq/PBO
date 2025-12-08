from models.account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, number, holder, balance=0.0, interest_rate=0.02):
        super().__init__(number, holder, balance)
        self.__interest_rate = interest_rate  # bunga per transaksi

    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"💰 Bunga {self.__interest_rate*100:.1f}% ditambahkan untuk {self.get_account_holder()}.")

    def account_type(self):
        return "Savings Account"

