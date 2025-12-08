class Buku:
    def __init__ (self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = False #tersedia

    def tampilkan_info(self):
        print("\n--- informasi buku ---")
        print(f"Judul Buku = {self.judul}")
        print(f"Penulis = {self.penulis}")
        print(f"Tahun Terbit = {self.tahun_terbit}")
        print(f"Status Pinjam = {self.status_pinjam}")

    def pinjam_buku(self):
        self.status_pinjam = True
        print(f"Judul Buku = {self.judul}")
        print(f"Penulis = {self.penulis}")
        print(f"Tahun Terbit = {self.tahun_terbit}")
        print(f"Status Pinjam = {self.status_pinjam}")
        print(f"buku {self.judul} telah dipinjam")

    def kembalikan_buku(self):
        self.status_pinjam = False
        print(f"buku {self.judul} sudah kemabli")
        
buku1 = Buku("Bungou Stray Dogs", "Kafka Asagiri", 2016)
buku2 = Buku("Crime and Punishment", "Fyodor Dostoyevsky", 1866)

print("\n--- Informasi Buku ---")
buku1.tampilkan_info()
print()
buku2.tampilkan_info()

print("\n--- peminjaman buku ---")
buku1.pinjam_buku()
print()
buku2.pinjam_buku()

print("\n--- pengembalian buku ---")
buku1.kembalikan_buku()
buku2.kembalikan_buku()

print("\n--- Informasi Buku ---")
buku1.tampilkan_info()
print()
buku2.tampilkan_info()