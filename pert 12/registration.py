import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

# KONFIGURASI LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger('Register')


# MODEL DATA
@dataclass
class RegistrationData:
    """
    Menyimpan data registrasi mahasiswa.

    Attributes:
        mahasiswa (str): Nama mahasiswa.
        total_sks (int): Total SKS yang diambil.
        matkul_diambil (List[str]): Daftar mata kuliah yang diambil.
        prasyarat_lulus (List[str]): Daftar mata kuliah yang telah lulus.
        jadwal (List[tuple]): Jadwal mata kuliah (hari, jam).
        ip_last_semester (Optional[float]): IP semester terakhir.
    """
    mahasiswa: str
    total_sks: int
    matkul_diambil: List[str]
    prasyarat_lulus: List[str]
    jadwal: List[tuple]
    ip_last_semester: Optional[float] = None


# ABSTRAKSI VALIDATION RULE (OCP + DIP)
class IValidationRule(ABC):
    """
    Kontrak untuk semua aturan validasi registrasi.
    """

    @abstractmethod
    def validate(self, data: RegistrationData) -> tuple[bool, Optional[str]]:
        """
        Melakukan validasi terhadap data registrasi.

        Args:
            data (RegistrationData): Data registrasi mahasiswa.

        Returns:
            tuple[bool, Optional[str]]:
            Status validasi dan pesan kesalahan (jika ada).
        """
        pass


# IMPLEMENTASI RULE (SRP)
class SksLimitRule(IValidationRule):
    """Validasi batas maksimum SKS."""

    def validate(self, data: RegistrationData):
        if data.total_sks > 24:
            logger.warning("SKS melebihi batas maksimum.")
            return False, f"SKS melebihi batas (maks 24). Kamu ambil {data.total_sks}."
        logger.info("Validasi SKS berhasil.")
        return True, None


class PrerequisiteRule(IValidationRule):
    """Validasi kelulusan prasyarat mata kuliah."""

    def validate(self, data: RegistrationData):
        for mk in data.matkul_diambil:
            if mk not in data.prasyarat_lulus:
                logger.warning("Prasyarat belum terpenuhi.")
                return False, f"Prasyarat belum terpenuhi untuk mata kuliah: {mk}"
        logger.info("Validasi prasyarat berhasil.")
        return True, None

class JadwalBentrokRule(IValidationRule):
    """Validasi bentrok jadwal mata kuliah."""

    def validate(self, data: RegistrationData):
        seen = set()
        for hari, jam in data.jadwal:
            key = (hari, jam)
            if key in seen:
                logger.warning("Jadwal bentrok terdeteksi.")
                return False, f"Jadwal bentrok pada hari {hari} jam {jam}"
            seen.add(key)
        logger.info("Validasi jadwal berhasil.")
        return True, None


class IPSemesterRule(IValidationRule):
    """Validasi IP semester terakhir terhadap batas SKS."""

    def validate(self, data: RegistrationData):
        if data.ip_last_semester is not None and data.ip_last_semester < 2.0:
            if data.total_sks > 18:
                logger.warning("IP rendah, SKS terlalu banyak.")
                return False, "IP rendah. Maksimal hanya boleh ambil 18 SKS."
        logger.info("Validasi IP semester berhasil.")
        return True, None

# REGISTRATION SERVICE (KOORDINATOR)
class RegistrationService:
    """
    Mengkoordinasikan proses validasi registrasi mahasiswa
    menggunakan dependency injection.
    """

    def __init__(self, rules: List[IValidationRule]):
        """
        Args:
            rules (List[IValidationRule]): Daftar aturan validasi.
        """
        self.rules = rules

    def validate(self, data: RegistrationData) -> tuple[bool, str]:
        """
        Menjalankan seluruh rule validasi.

        Args:
            data (RegistrationData): Data registrasi mahasiswa.

        Returns:
            tuple[bool, str]: Status dan pesan hasil validasi.
        """
        logger.info("Memulai proses validasi registrasi.")
        for rule in self.rules:
            is_valid, message = rule.validate(data)
            if not is_valid:
                return False, message or "Validasi gagal"

        logger.info("Semua validasi berhasil.")
        return True, "Registrasi berhasil!"

data = RegistrationData(
    mahasiswa="Budi",
    total_sks=20,
    matkul_diambil=["PBO", "Basis Data"],
    prasyarat_lulus=["PBO", "Basis Data"],
    jadwal=[("Senin", "08.00-10.00"), ("Rabu", "10.00-12.00")],
    ip_last_semester=2.5
)

rules = [
    SksLimitRule(),
    PrerequisiteRule(),
    JadwalBentrokRule(),
    IPSemesterRule()
]

service = RegistrationService(rules)
result = service.validate(data)
print(result)
