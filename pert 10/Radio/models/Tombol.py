class Tombol:
    def __init__(self, fungsi):
        self._fungsi = fungsi

    def ditekan(self):
        print(f"Tombol '{self._fungsi}' **Ditekan**.")
        return True
    
# asosisasi (alat bantu, dapat diganti/digunakan dengan yg lain)