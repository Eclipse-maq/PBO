# DEBUG REPORT – Bug PPN 10%

## Deskripsi Bug
Ditemukan perbedaan hasil perhitungan harga akhir pada fungsi `hitung_diskon`.
Harga akhir lebih besar dari hasil yang seharusnya setelah diskon diterapkan.

## Langkah Debugging Menggunakan pdb

1. Menambahkan breakpoint menggunakan `pdb.set_trace()` pada awal fungsi `hitung_diskon`.
2. Menjalankan unit test hingga program berhenti di debugger.
3. Memeriksa nilai variabel menggunakan perintah pdb.

## Hasil Pemeriksaan Variabel

```bash
(Pdb) p harga_awal
1000
(Pdb) p persentase_diskon
10
(Pdb) p jumlah_diskon
100.0
(Pdb) p harga_akhir
900.0
(Pdb) n
(Pdb) p harga_akhir
990.0

Dari hasil tersebut terlihat bahwa nilai harga_akhir awalnya bernilai 900, yang merupakan hasil diskon 10% dari 1000. Namun setelah melanjutkan eksekusi satu baris berikutnya (n), nilai harga_akhir berubah menjadi 990. Perubahan ini membuktikan bahwa terdapat penambahan PPN 10% yang diterapkan kembali pada harga yang sudah didiskon.

Kesimpulannya, bug terjadi karena harga akhir dikenakan PPN 10% secara tidak disengaja setelah proses diskon, sehingga PPN dihitung dua kali. Bug ini diperbaiki dengan menghapus baris kode yang menambahkan PPN pada fungsi hitung_diskon.