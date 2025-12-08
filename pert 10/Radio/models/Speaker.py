class Speaker:
    def __init__(self):
        self._volume = 50
        print("Speaker Radio disiapkan.")

    def set_volume(self, level):
        self._volume = max(0, min(100, level))
        print(f"Volume diatur ke: {self._volume}")

    # mengubah status Speaker (berdasarkan input Radio)
    def putar_suara(self, info_stasiun):
        if self._volume > 0:
            print(f"Speaker memutar: {info_stasiun} [Vol: {self._volume}]")
        else:
            print("Speaker senyap. (Volume 0)")

# komposisi (tidak akan berfungsi sebagai speaker tanpa radio)