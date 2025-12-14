# inf2143 proyek solid oop python
# pert 12, dokumentasi dan version control

### Deskripsi proyek
proyek ini mendemonstrasikan implementasi prinsip solid (srp, ocp, dip) pada sistem checkout dengan menggunakan abstration (interface) dan dependency injection

### struktur file 
- `refactor_solid.py`: kode inti yang sudah direfaktor dan ditambahkan logging
- `readme.md`: dokumen ini


# Sistem Validasi Registrasi Mahasiswa Berbasis SOLID

## Deskripsi
Proyek ini merupakan implementasi sistem validasi registrasi mahasiswa yang dirancang menggunakan prinsip-prinsip **Object-Oriented Programming (OOP)** dan **SOLID**. Sistem ini bertujuan untuk memvalidasi data registrasi mahasiswa secara modular, terstruktur, dan mudah dikembangkan dengan memanfaatkan konsep **Dependency Injection** dan **rule-based validation**.

Sistem ini memvalidasi beberapa aspek penting dalam proses registrasi mahasiswa, antara lain batas jumlah SKS, pemenuhan prasyarat mata kuliah, bentrok jadwal, serta IP semester terakhir.

--

## Tujuan Pengembangan
Pengembangan sistem ini bertujuan untuk:
1. Menghilangkan *code smell* berupa penggunaan struktur `if/else` yang berlebihan.
2. Menerapkan **Single Responsibility Principle (SRP)** dengan memisahkan setiap aturan validasi ke dalam class tersendiri.
3. Menerapkan **Open/Closed Principle (OCP)** agar sistem dapat diperluas tanpa mengubah kode yang sudah ada.
4. Menerapkan **Dependency Inversion Principle (DIP)** dengan membuat service bergantung pada abstraksi.
5. Mengimplementasikan dokumentasi kode (*docstring*) dan *logging* sebagai bagian dari praktik pemrograman yang baik.

--

## Analisis Kode Sebelum Refactoring

Pada versi awal sistem, seluruh proses validasi dilakukan di dalam satu kelas (`ValidatorManager`). Pendekatan ini menimbulkan beberapa permasalahan desain sebagai berikut:

### Pelanggaran Single Responsibility Principle (SRP)
Satu kelas memiliki terlalu banyak tanggung jawab, seperti memvalidasi SKS, prasyarat mata kuliah, jadwal, dan IP semester. Hal ini menyebabkan kode sulit dipelihara dan rawan kesalahan saat dilakukan perubahan.

### Pelanggaran Open/Closed Principle (OCP)
Setiap penambahan aturan validasi baru mengharuskan perubahan pada kode yang sudah ada. Kelas utama tidak tertutup terhadap modifikasi, sehingga berisiko menimbulkan bug baru.

### Pelanggaran Dependency Inversion Principle (DIP)
Kelas utama bergantung langsung pada detail implementasi logika validasi, bukan pada abstraksi. Hal ini menyulitkan pengujian dan pengembangan lebih lanjut.

---

## Desain Sistem Setelah Refactoring

### Arsitektur Berbasis Rule
Setelah refactoring, sistem menggunakan pendekatan *rule-based validation*. Setiap aturan validasi direpresentasikan sebagai class yang mengimplementasikan interface `IValidationRule`.

```python
class IValidationRule(ABC):
    @abstractmethod
    def validate(self, data: RegistrationData) -> tuple[bool, Optional[str]]:
        pass
````

Dengan pendekatan ini, setiap rule memiliki satu tanggung jawab yang jelas.

---

## Implementasi Single Responsibility Principle (SRP)

Setiap aturan validasi diimplementasikan dalam class terpisah, antara lain:

* `SksLimitRule` untuk memvalidasi batas maksimum SKS.
* `PrerequisiteRule` untuk memvalidasi prasyarat mata kuliah.
* `JadwalBentrokRule` untuk mendeteksi bentrok jadwal.
* `IPSemesterRule` untuk membatasi SKS berdasarkan IP semester terakhir.

Masing-masing class hanya berfokus pada satu jenis validasi, sehingga perubahan pada satu aturan tidak memengaruhi aturan lain.

---

## Implementasi Dependency Inversion Principle (DIP)

Proses validasi dikoordinasikan oleh `RegistrationService`. Kelas ini tidak mengetahui detail implementasi aturan validasi, melainkan hanya bergantung pada abstraksi `IValidationRule`.

```python
class RegistrationService:
    def __init__(self, rules: List[IValidationRule]):
        self.rules = rules
```

Aturan validasi disuntikkan melalui constructor (*Dependency Injection*), sehingga sistem menjadi fleksibel dan mudah dikembangkan.

---

## Pembuktian Open/Closed Principle (OCP)

Penambahan aturan baru, seperti validasi IP semester (`IPSemesterRule`), dilakukan tanpa mengubah kode:

* `RegistrationService`
* Rule lain yang sudah ada

Cukup dengan membuat class rule baru dan menambahkannya ke daftar rule saat inisialisasi. Hal ini membuktikan bahwa sistem terbuka untuk ekstensi dan tertutup untuk modifikasi.

---

## Logging

Seluruh output sistem menggunakan modul `logging` sebagai pengganti `print()`. Logging dikonfigurasi satu kali di entry point aplikasi:

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
```

Logging digunakan untuk mencatat:

* Proses validasi yang berhasil (`INFO`)
* Kegagalan validasi (`WARNING`)

Pendekatan ini membuat sistem lebih profesional dan mudah ditelusuri saat debugging.

---

## Struktur Data

Data registrasi mahasiswa direpresentasikan menggunakan `@dataclass` sebagai berikut:

```python
@dataclass
class RegistrationData:
    mahasiswa: str
    total_sks: int
    matkul_diambil: List[str]
    prasyarat_lulus: List[str]
    jadwal: List[tuple]
    ip_last_semester: Optional[float] = None
```

Penggunaan `Optional` memastikan kompatibilitas dengan *static type checker* seperti Pylance.

---

## Kesimpulan

Setelah dilakukan refactoring, sistem validasi registrasi mahasiswa memiliki struktur yang lebih bersih, modular, dan mudah dikembangkan. Penerapan prinsip SOLID berhasil menghilangkan *code smell*, meningkatkan keterbacaan kode, serta mempermudah penambahan fitur baru tanpa merusak kode yang sudah ada.

Pendekatan Dependency Injection terbukti lebih efektif dibandingkan penggunaan struktur `if/else` konvensional dalam menjaga kualitas desain perangkat lunak.
