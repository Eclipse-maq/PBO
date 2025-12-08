from datetime import datetime

class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []

    def add_account(self, account):
        self.__accounts.append(account)
        print(f"✅ Akun {account.get_account_number()} milik {account.get_account_holder()} berhasil ditambahkan.")

    def all_accounts(self):
        return self.__accounts

    def find_account(self, number):
        for acc in self.__accounts:
            if acc.get_account_number() == number:
                return acc
        return None

    def show_summary(self):
        print(f"\n=== Ringkasan Bank {self.__name} ===")
        total = 0
        for acc in self.__accounts:
            print(f"{acc.get_account_number()} | {acc.get_account_holder()} | Saldo: Rp{acc.get_balance():,.2f}")
            total += acc.get_balance()
        print(f"Total Dana: Rp{total:,.2f}")

    def get_name(self):
        return self.__name

    def log_activity(self, msg):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] {msg}")
