from models.Buku import Buku
from models.Pustaka import Pustaka
from models.Anggota import Anggota

buku1 = Buku("Harry Potter", "J.K. Rowling")
buku2 = Buku("The Hobbit", "J.R.R. Tolkien")

pustaka = Pustaka()
pustaka.tambah_buku(buku1)
pustaka.tambah_buku(buku2)

anggotal = Anggota("Andi")
anggotal.pinjam_buku(buku1)
anggotal.pinjam_buku(buku2)

print("\nStatus Koleksi Pustaka:")
pustaka.tampilkan_koleksi()

anggotal.kembalikan_buku(buku1)
print("\nStatus Koleksi Setelah Pengembalian:")
pustaka.tampilkan_koleksi()