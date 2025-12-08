class Notifikasi:
    def kirim(self, pesan):
        raise NotImplementedError("subclass harus mengimplementasikan method ini")

class Email(Notifikasi):
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")

class SMS(Notifikasi):
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")

class PushNotif(Notifikasi):
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")

daftar_notifikasi = [Email(), SMS(), PushNotif()]

for notif in daftar_notifikasi:
    notif.kirim("diskon spesial! hanya untuk anda")