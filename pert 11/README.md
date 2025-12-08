# Analisis Pelanggaran Prinsip SOLID dalam Kode Registrasi Mahasiswa

Proyek ini mendemonstrasikan analisis pelanggaran prinsip SOLID (SRP, OCP, DIP) dalam kode validasi registrasi mahasiswa, serta refactoring untuk mengatasi pelanggaran tersebut.

## Deskripsi Kode
Kode ini berisi:
- **God Class (Sebelum Refactor)**: Kelas `ValidatorManager` yang menangani semua validasi dalam satu tempat.
- **Refactoring**: Penggunaan interface `IValidationRule`, kelas-kelas rule spesifik, dan `RegistrationService` untuk orkestrasi validasi.

## Analisis Pelanggaran SOLID

### 1. Single Responsibility Principle (SRP)
- **Pelanggaran**: `ValidatorManager` menangani validasi SKS, prasyarat, jadwal, dan IP sekaligus.
- **Perbaikan**: Setiap rule (e.g., `SksLimitRule`) memiliki satu tanggung jawab. `RegistrationService` mengorkestrasi tanpa melakukan validasi sendiri.

### 2. Open-Closed Principle (OCP)
- **Pelanggaran**: Menambah validasi baru memerlukan modifikasi `ValidatorManager`.
- **Perbaikan**: Tambah kelas rule baru yang implement `IValidationRule`, tanpa ubah kode existing. Inject rules ke `RegistrationService`.

### 3. Dependency Inversion Principle (DIP)
- **Pelanggaran**: `ValidatorManager` bergantung langsung pada implementasi validasi.
- **Perbaikan**: `RegistrationService` bergantung pada abstraksi `IValidationRule`. Rules diinject, memungkinkan fleksibilitas dan testing.

## Kesimpulan
Refactoring ini membuat kode lebih maintainable, extensible, dan testable. Untuk detail lebih lanjut, lihat kode sumber.
```