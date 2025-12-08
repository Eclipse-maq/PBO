class Stasiun:
    def __init__(self, nama, frekuensi):
        self._nama = nama
        self._frekuensi = frekuensi

    def get_info(self):
        return f"Stasiun: {self._nama} ({self._frekuensi} MHz)" # mengembalikan informasi
    
# agregasi (bisa berdiri sendiri tanpa radio)