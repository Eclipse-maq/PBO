from models.account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, number, holder, balance=0.0, overdraft_limit=50000):
        super().__init__(number, holder, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # override → polymorphism
        if amount <= 0:
            print("❌ Jumlah tarik tidak valid.")
            return
        if amount > self.get_balance() + self.__overdraft_limit:
            print(f"❌ {self.get_account_holder()} melebihi batas overdraft!")
            return
        # tetap boleh minus asal tidak melebihi limit
        self._BankAccount__balance = self.get_balance() - amount
        self._BankAccount__record_transaction("Penarikan (Overdraft)", -amount)
        print(f"⚠️ {self.get_account_holder()} menarik Rp{amount:,.2f} (Overdraft diizinkan).")

    def account_type(self):
        return "Checking Account"