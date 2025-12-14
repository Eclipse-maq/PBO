import logging
# berada di awal file

# konfig dasar: semua log level info ke atas akan ditampilkan
# format: waktu = level - - nama kelas/fungsi - pesan
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
# tambahkan logger untuk kelas yang akan digunakan
LOGGER = logging.getLogger('Checkout')

# mendefinisikan kode yang bermasalah (the god class)
from abc import ABC, abstractmethod
from dataclasses import dataclass


# model sederhana
@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

# === kode buruk (sebelum refactor) ===
class OrderManager: # melanggar srp, ocp, dip
    def process_checkout(self, order: Order, payment_method: str):
        print(f"memulai checkout untuk {order.customer_name}...")

        # logika pembayaran (pelanggaran ocp/dip)
        if payment_method == "credit_card":
            # logika detail implementasi hardcoded di sini
            print("processing credit card...")
        elif payment_method == "bank_transfer":
            # logika detail implementasi hardcoded di sini
            print("processing bank transfer...")
        else:
            print("metode tidak valid")
            return False
        
        # logika notifikasi (pelanggaran srp)
        print(f"mengirim notifikasi ke {order.customer_name}...")
        order.status = "paid"
        return True

# refactoring srp dan dip (membuat kontak)
# ---  abstraksi (kontrak untuk ocp/dip) ---
class IPaymentProcessor(ABC):
    """kontrak: semua processor pembayaran harus punya method 'proces'."""
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass

class INotificationService(ABC):
    """kontrak: semua layanan notifikasi harus punya method 'send'."""
    @abstractmethod
    def send(self, order: Order):
        pass

#--- implementasi konkrit (plug-in) ---
class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("payment: memproses kartu kredit.")
        return True

class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"notif: mengirim email konfirmasi ke {order.customer_name}")

#--- kelas koordinator (srp & dip) ---
class CheckouitService: #tanggung jawab tunggal: mengkoordinasi checkout
    """
    kelas high-level untuk mengkoordinasi proses transaksi pembayaran
    kelas ini memisahkan logika pembayaran dan notifikasi (memenuhi srp)
    """
    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        """
        menginisialisasi checkoutservice dengan dependensi yang diperlukan

        args:
            payment_processor (IPaymentProcessor): implementasi interface pembayaran
            notifier (INotificationService): implementasi interface notifikasi
        """
        # dependency injection (dip): bergantung pada abstraksi, bukan konkrit
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order):
        # logging alih alih print()
        LOGGER.info(f"Memulai checkout untuk {order.customer_name}. Total: {order.total_price}")

        payment_success = self.payment_processor.process(order) # delegasi 1

        if payment_success:
            order.status = "paid"
            self.notifier.send(order) # delegasi 2
            LOGGER.info("Checkout sukses. Status pesanan: PAID")
            return True
        else:
            # gunakan level error/warning untuk masalah
            LOGGER.error("Pembayaran gagal. Transaksi dibatalkan")
            return False
    
# Eksekusi dan pembuktian ocp
#--- program utama ---
# setup dependencies
andi_order = Order("Andi", 500000)
email_service = EmailNotifier()

# 1. inject implementasi credit card
cc_processor = CreditCardProcessor()
checkout_cc = CheckouitService(payment_processor=cc_processor, notifier=email_service)
print("--- skenario 1: Credit card ---")
checkout_cc.run_checkout(andi_order)

# 2. pembuktian ocp: menambah metode pembayaran qris (tanpa mengubah checkoutservice)
class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("payment: memproses QRIS")
        return True
    
budi_order = Order("budi", 100000)
qris_processor = QrisProcessor()

# inject implementasi QRIS yang baru dibuat
checkout_qris = CheckouitService(payment_processor=qris_processor, notifier=email_service)
print("\n--- skenario 2: pembuktian ocp (QRIS) ---")
checkout_qris.run_checkout(budi_order)