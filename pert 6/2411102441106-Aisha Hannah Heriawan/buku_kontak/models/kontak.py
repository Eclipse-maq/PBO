class Kontak:
    def __init__(self, nama, nomor_telepon):
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon
    
    def tampilkan_info(self):
        print(f"Nama: {self.__nama}, Nomor Telepon: {self.__nomor_telepon}")
    
    # Getter dan Setter untuk nama
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama_baru):
        self.__nama = nama_baru
    
    # Getter dan Setter untuk nomor_telepon
    def get_nomor_telepon(self):
        return self.__nomor_telepon
    
    def set_nomor_telepon(self, nomor_baru):
        self.__nomor_telepon = nomor_baru