class Karyawan:
    def __init__(self, nama, id_karyawan, gaji):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji

    def info(self):
        print(f"Nama\t: {self.__nama}\nID\t: {self.__id_karyawan}\nGaji\t: {self.__gaji}")

    # Getter
    def get_nama(self):
        return self.__nama
    
    def get_id_karyawan(self):
        return self.__id_karyawan
    
    def get_gaji(self):
        return self.__gaji
    
    # Setter
    def set_nama(self, nama_baru):
        if len(nama_baru) > 3:
            self.__nama = nama_baru
            print("nama berhasil diubah")
        else:
            print("nama terlalu pendek, min 3 karakter lah")

    def set_gaji(self, gaji_baru):
        if gaji_baru < 0:
            print("gaji tidak bisa negatif")
        else:
            self.__gaji = gaji_baru

karyawan1 = Karyawan("Aisha", "2411102441106", 50000000)
karyawan1.info()

print("\n-- ubah lewat setter --") # gagal
karyawan1.set_nama("")
karyawan1.set_gaji(-600000)
karyawan1.info()

print("\n-- ubah lewat setter --") # berhasil
karyawan1.set_nama("Hana")
karyawan1.set_gaji(600000)
karyawan1.info()