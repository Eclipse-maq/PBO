from models.Speaker import Speaker
from models.Tombol import Tombol

class Radio:
    def __init__(self, daftar_stasiun, stasiun_awal_index=0):
        self._speaker = Speaker()
        self._daftar_stasiun = daftar_stasiun
        self._indeks_stasiun_aktif = stasiun_awal_index
        self._tombol_tune = Tombol("Next")        
        print("Radio Digital dihidupkan.")

    def putar_stasiun(self):
        stasiun_aktif = self._daftar_stasiun[self._indeks_stasiun_aktif]
        info = stasiun_aktif.get_info() 
        self._speaker.putar_suara(info)

    def ganti_stasiun(self):
        if self._tombol_tune.ditekan():
            self._speaker.set_volume(40) 
            self._indeks_stasiun_aktif = (self._indeks_stasiun_aktif + 1) % len(self._daftar_stasiun)
            print(f"Radio sedang tuning... ninung ninung eaa...")
            self.putar_stasiun()