import math
import datetime

class KalkulatorLingkaran:
    def __init__(self, radius):
        self.__radius = 0
        self.set_radius(radius)
        print(f"Objek Lingkaran dengan radius {self.__radius} dibuat.")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("error: radius harus lebih besar dari 0.")
            self.__radius = 1

    def hitung_luas(self):
        luas = math.pi * (self.__radius ** 2)
        return luas
    
    def hitung_keliling(self):
        keliling = 2 * math.pi * self.__radius
        return keliling
    
# --- bagian utama program ---
lingkaran_1 = KalkulatorLingkaran(7)
luas_lingkaran = lingkaran_1.hitung_luas()
keliling_lingkaran = lingkaran_1.hitung_keliling()

print(f"\nRadius: 7")
print(f"luas lingkaran: {luas_lingkaran:.2f}")
print(f"keliling_lingkaran: {keliling_lingkaran:.2f}")

class LogPesan:
    def __init__(self, pengirim, isi_pesan):
        self.__pengirim = pengirim
        self.__isi_pesan = isi_pesan
        self.__timestamp = datetime.datetime.now()

    def tampilan_log(self):
        waktu_terformat = self.__timestamp.strftime("%D %B %Y, pukul %H:%M:%S")
        print("\n--- Log Pesan Masuk ---")
        print(f"pengirim\t: {self.__pengirim}")
        print(f"waktu\t\t: {waktu_terformat}")
        print(f"pesan\t\t: {self.__isi_pesan}")

pesan1 = LogPesan("Admin", "server akan segera di restart ntuk maintenance")
pesan1.tampilan_log()

pesan2 = LogPesan("User1", "Pekerjan saya sudah disimpan, silahkan restart")
pesan2.tampilan_log()