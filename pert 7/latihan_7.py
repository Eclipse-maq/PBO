import os
import datetime

class FileAnalyzer:
    def __init__(self, file_path):
        if os.path.exists(file_path):
            print("File ditemukan!")
            self.__file_path = file_path
            self.__file_size = os.path.getsize(file_path)
            self.__file_ada = True
        else:
            print(f"Error: File '{file_path}' tidak ditemukan.")
            self.__file_ada = False
    
    def get_file_size(self, unit="bytes"):
        if not self.__file_ada:
            return None
        
        if unit == "bytes":
            return self.__file_size
        elif unit == "KB":
            return self.__file_size / 1024
        else:
            print("error: unit tidak valid. gunakan 'bytes' atau 'KB'.")
            return None
    
    def get_modification_time(self):
        if not self.__file_ada:
            return None
        
        mod_time = os.path.getmtime(self.__file_path)
        readable_time = datetime.datetime.fromtimestamp(mod_time)
        return readable_time
    
    def analyze(self):
        if not self.__file_ada:
            print("tidak dapat dianalisis karena tidak ditemukan.")
            return
        
        file_name = os.path.basename(self.__file_path)
        file_size_kb = self.get_file_size("KB")
        mod_time = self.get_modification_time()
        
        print("=== Laporan Analisis File ===")
        print(f"Nama File: {file_name}")
        print(f"File Ada: Ya")
        print(f"Ukuran File: {file_size_kb:.2f} KB")
        print(f"Waktu Modifikasi Terakhir: {mod_time}")
        print("=" * 30)

file_path = "pert 7/dokumen.txt"
analyzer = FileAnalyzer(file_path)
analyzer.analyze()