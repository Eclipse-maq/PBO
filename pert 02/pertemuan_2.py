class Mahasiswa:
    #konstruktor
    def __init__(self, input_nama, input_nim, input_prodi):
        self.nama = input_nama
        self.nim = input_nim
        self.prodi = input_prodi
        print(f"objek mahasiswa dengan nama {self.nama} telah dibuat")

    def sapa(self):
        print(f"halo nama saya {self.nama}. senang berkenalan")

    def tampilkan_info(self):
        print("--- informasi mahasiswa ---")
        print(f"nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"prodi   : {self.prodi}")
        print("----------------------------")

#mmbuat objek
otong = Mahasiswa("otong surotong", "12345", "tekniik informatika")
ucup = Mahasiswa("ucup surucup", "67890", "sistem infromasi")

#method dri masing masinng objek
print("\n--- interaksi dengan objek ---")
otong.sapa()
ucup.sapa()

print("\n--- meminta objek enampilkan datanya ---")
otong.tampilkan_info()
ucup.tampilkan_info()

#akses atribut
print("\n--- Data Mahasiswa ---")
print(f"data mahasiswa 1: {otong.nama} - {otong.nim} - {otong.prodi}")
print(f"data mahasiswa 2: {ucup.nama} - {ucup.nim} - {ucup.prodi}")