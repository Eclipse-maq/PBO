class Kendaraan:
    def __init__(self, merk, tahun_produksi, warna):
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    def tampilkan_info(self):
        print(f"Merk\t\t: {self.__merk}")
        print(f"Produksi\t: {self.__tahun_produksi}")
        print(f"Warna\t\t: {self.__warna}")

    def nyalakan_mesin(self):
        print("Mesin kendaraan menyala")

class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, jumlah_pintu):
        super().__init__(merk, tahun_produksi, warna)
        self.__jumlah_pintu = jumlah_pintu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jumlah pintu\t: {self.__jumlah_pintu}")

    def buka_pintu_bagasi(self):
        print("pintu bagasi dibuka")

class Motor(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, kapasitas_tangki):
        super().__init__(merk, tahun_produksi, warna)
        self.__kapasitas_tangki = kapasitas_tangki

    def nyalakan_mesin(self):
        print("BRMMM... Mesin motor dinyalakan dengan kick starter")

    def isi_bensin(self):
        print(f"tangki diisi, kapasitas tangki {self.__kapasitas_tangki} liter")

mobil1 = Mobil("toyota avanza", 2020, "putih", 4)
motor1 = Motor("honda beat", 2022, "pink", 4)

print("=== Info Mobil ===")
mobil1.tampilkan_info()
mobil1.nyalakan_mesin()
mobil1.buka_pintu_bagasi()

print("\n=== Info Motor ===")
motor1.tampilkan_info()
motor1.nyalakan_mesin()
motor1.isi_bensin()