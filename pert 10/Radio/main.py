from models.Radio import Radio
from models.Stasiun import Stasiun

stasiun_a = Stasiun("Radio Edukasi", 107.0)
stasiun_b = Stasiun("Radio Musik Pop", 99.8)
stasiun_c = Stasiun("Radio Berita", 88.0)
daftar_stasiun = [stasiun_a, stasiun_b, stasiun_c]

radio_saya = Radio(daftar_stasiun) 

print("\n--- Putaran Awal ---")

# memutar stasiun pertama
radio_saya.putar_stasiun()

print("\n--- Ganti Stasiun ---")

# ganti stasiun
radio_saya.ganti_stasiun()

# ganti stasiun 
radio_saya.ganti_stasiun()