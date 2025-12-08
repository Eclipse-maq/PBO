from datetime import datetime

class BankAccount:
    def __init__(self, number, holder, balance=0.0):
        self.__account_number = number
        self.__account_holder = holder
        self.__balance = balance
        self.__transactions = []

    # Getter
    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    # Public methods
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Jumlah setor tidak valid.")
            return
        self.__balance += amount
        self.__record_transaction("Setoran", amount)
        print(f"✅ {self.__account_holder} menyetor Rp{amount:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Jumlah tarik tidak valid.")
            return
        if amount > self.__balance:
            print(f"❌ Saldo {self.__account_holder} tidak mencukupi.")
            return
        self.__balance -= amount
        self.__record_transaction("Penarikan", -amount)
        print(f"💸 {self.__account_holder} menarik Rp{amount:,.2f}")

    def __record_transaction(self, jenis, amount):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transactions.append(f"{ts} - {jenis}: Rp{amount:,.2f}")

    def get_transactions(self):
        return self.__transactions

    def __str__(self):
        return f"{self.__account_number} ({self.__account_holder}) - Rp{self.__balance:,.2f}"
