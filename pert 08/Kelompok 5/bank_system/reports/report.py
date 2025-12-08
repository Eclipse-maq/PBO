import os
from datetime import datetime

REPORT_DIR = "reports_output"
REPORT_FILE = os.path.join(REPORT_DIR, "laporan.txt")

def ensure_report_dir():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

def generate_report(bank, title="Laporan UTS PBO - Bank Simulation"):
    ensure_report_dir()
    accounts = bank.all_accounts()
    total = sum(acc.get_balance() for acc in accounts)
    avg = total / len(accounts) if accounts else 0

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        f"{title}",
        f"Generated: {ts}",
        f"Bank: {bank.get_name()}",
        f"Total Akun: {len(accounts)}",
        f"Total Saldo: Rp{total:,.2f}",
        f"Rata-rata Saldo: Rp{avg:,.2f}",
        "",
        "Detail Akun:"
    ]

    for acc in accounts:
        lines.append(f"- {acc.get_account_number()} | {acc.get_account_holder()} | {acc.account_type()} | Saldo: Rp{acc.get_balance():,.2f}")

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nLaporan berhasil dibuat di: {REPORT_FILE}")
