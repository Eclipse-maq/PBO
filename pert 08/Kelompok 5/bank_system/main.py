from models.bank import Bank
from models.savings_account import SavingsAccount
from reports.report import generate_report

if __name__ == "__main__":
    bank = Bank("Bank Kelompok 5")

    # buat akun
    acc1 = SavingsAccount("ACC001", "Aisha", 200000, 0.05)
    acc2 = SavingsAccount("ACC002", "Hana", 100000, 50000)
    acc3 = SavingsAccount("ACC003", "Kampoel", 50000, 0.03)

    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)

    # simulasi transaksi
    acc1.deposit(80000)
    acc1.apply_interest()
    acc2.withdraw(120000)
    acc3.deposit(100000)
    acc3.apply_interest()

    # tampilkan ringkasan
    bank.show_summary()

    # buat laporan ke file
    generate_report(bank, title="Laporan Bank Kelompok 5")
