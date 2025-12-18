import pdb

class DiskonCalculator:
    """menghitung harga akhir setelah diskon"""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # pdb.set_trace() <- untuk debugging: tempatkan disini
        
        # --- bug logika ---
        # persentase tidak dibagi 100, sehingga diskon 10% dihitung sebagai 1000%
        # jumlah_diskon = harga_awal * persentase_diskon

        # code perbaikan
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_akhir = harga_awal - jumlah_diskon
        return harga_akhir
    
# --- uji coba ( ini adalah test case yuang akan gagal )
if __name__ == '__ main__':
    calc = DiskonCalculator()
    # input: 1000 - 10%. hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"hasil: {hasil}")
    # output: hasil = -9000.0 {salah}