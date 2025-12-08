from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple, Optional, List, Any

@dataclass
class RegistrationData:
    mahasiswa: str
    total_sks: int
    matkul_diambil: list
    prasyarat_lulus: list
    jadwal: list
    ip_last_semester: float = None

# god class (sebelum refactor)
class ValidatorManager:
    def validate(self, data: RegistrationData):

        if data.total_sks > 24:
            return False, f"SKS melebihi batas (maks 24). Kamu ambil {data.total_sks}."

        for mk in data.matkul_diambil:
            if mk not in data.prasyarat_lulus:
                return False, f"Prasyarat belum terpenuhi untuk mata kuliah: {mk}"

        seen = set()
        for hari, jam in data.jadwal:
            key = (hari, jam)
            if key in seen:
                return False, f"Jadwal bentrok pada hari {hari} jam {jam}!"
            seen.add(key)

        if data.ip_last_semester is not None and data.ip_last_semester < 2.0:
            if data.total_sks > 18:
                return False, "IP rendah. Maksimal hanya boleh ambil 18 SKS."

        return True, "Registrasi berhasil!"

# refactoring
# abstraksi
class IValidationRule(ABC):

    @abstractmethod
    def validate(self, data: RegistrationData) -> Tuple[bool, Optional[str]]:
        pass

# 4. RULE — sudah aman
class SksLimitRule(IValidationRule):
    def validate(self, data: RegistrationData):
        if data.total_sks > 24:
            return False, f"SKS melebihi batas (maks 24). Kamu ambil {data.total_sks}."
        return True, None


class PrerequisiteRule(IValidationRule):
    def validate(self, data: RegistrationData):
        for mk in data.matkul_diambil:
            if mk not in data.prasyarat_lulus:
                return False, f"Prasyarat belum terpenuhi untuk mata kuliah: {mk}"
        return True, None


class JadwalBentrokRule(IValidationRule):
    def validate(self, data: RegistrationData):
        seen = set()
        for hari, jam in data.jadwal:
            key = (hari, jam)
            if key in seen:
                return False, f"Jadwal bentrok pada hari {hari} jam {jam}!"
            seen.add(key)
        return True, None


class IPSemesterRule(IValidationRule):
    def validate(self, data: RegistrationData):
        if data.ip_last_semester is not None and data.ip_last_semester < 2.0:
            if data.total_sks > 18:
                return False, "IP rendah. Maksimal hanya boleh ambil 18 SKS."
        return True, None

class RegistrationService:
    def __init__(self, rules: List[IValidationRule]):
        self.rules = rules

    def _normalize(self, result: Any) -> Tuple[bool, Optional[str]]:
        # Jika kembaliannya tuple, langsung dipakai
        if isinstance(result, tuple):
            if len(result) != 2:
                raise RuntimeError(f"Rule mengembalikan tuple tapi panjangnya aneh: {result}")
            return result

        # Jika boolean saja, kita artikan sebagai valid/invalid tanpa pesan
        if isinstance(result, bool):
            return result, None

        # Kalau None atau tipe lain = implementasi rule salah
        raise RuntimeError(f"Rule mengembalikan nilai tidak valid: {result!r}")

    def validate(self, data: RegistrationData):
        for rule in self.rules:
            raw = rule.validate(data)
            is_valid, message = self._normalize(raw)
            if not is_valid:
                return False, message

        return True, "Registrasi berhasil!"

data = RegistrationData(
    mahasiswa="Budi",
    total_sks=26,
    matkul_diambil=["PBO", "Basis Data"],
    prasyarat_lulus=["Basis Data"],
    jadwal=[("Senin", "08.00-10.00"), ("Senin", "08.00-10.00")],
    ip_last_semester=1.8,
)

print("\n--- VALIDASI (GOD CLASS) ---")
print(ValidatorManager().validate(data))

rules = [
    SksLimitRule(),
    PrerequisiteRule(),
    JadwalBentrokRule(),
    IPSemesterRule(),
]

print("\n--- VALIDASI (SETELAH REFACTOR) ---")
print(RegistrationService(rules).validate(data))
