class Bentuk:
    def gambar(self):
        raise NotImplementedError("subclass harus menginplementasikan method ini")
    
class Persegi(Bentuk):
    def gambar(self):
        print("Menggambar Persegi: [][][]")

class Lingkaran(Bentuk):
    def gambar(self):
        print("Menggambar lingkaran: OOO")

class Segitiga(Bentuk):
    def gambar(self):
        print("menggambar segitiga: /\\")

class Teks:
    def gambar(self):
        print("Menulis teks: 'halo, poli'")

def render_objek(objek_untuk_digambar):
    print("mencoba merender objek...")
    objek_untuk_digambar.gambar()

daftar_bentuk = [Persegi(), Lingkaran(), Persegi(), Lingkaran()]
print("\n--- Memanggil method yang sama pada objek yag berbeda ---")

for bentuk in daftar_bentuk:
    bentuk.gambar()

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()
teks_biasa = Teks()

print("\n--- menggunakan fungsi polimorfik ---")
render_objek(persegi)
render_objek(lingkaran)
render_objek(segitiga)

print("\n--- Demonstrasikan Duck Typing ---")
render_objek(teks_biasa)