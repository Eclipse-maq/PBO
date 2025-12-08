from models.kontak import Kontak

if __name__ == "__main__":
    daftar_kontak = []
    
    kontak1 = Kontak("Aish", "081234567890")
    kontak2 = Kontak("Liam", "080987654321")
    kontak3 = Kontak("Louis", "081112223334")
    
    daftar_kontak.append(kontak1)
    daftar_kontak.append(kontak2)
    daftar_kontak.append(kontak3)
    
    for kontak in daftar_kontak:
        kontak.tampilkan_info()