class User:
    def __init__(self, username, level):
        self.__username = username
        self.__level = level

    def info(self):
        print(f"Username: {self.__username}. Level: {self.__level}")

    def get_username(self): # get untuk username
        return self.__username
    
    def get_level(self): # get untuk level
        return self.__level
    
    def set_username(self, username_baru):
        if len(username_baru) > 5:
            self.__username = username_baru
            print("username berhasil diubah")
        else:
            print("eror, username terlalu pendek! min 6 karakter")

    def set_level(self, level_baru):
        allowed_levels = ["bronze", "gold", "iridium", "myth"]
        if level_baru in allowed_levels:
            self.__level = level_baru
            print("level berhasil diubah")
        else:
            print(f"eror, level {level_baru} tidak valid")

user_1 = User("pengguna baru", "user")
user_1.info()

# Atribut bisa diubah seenaknya dari luar
print("\n[merusak data dari luar class]")
user_1.level = 12345
user_1.username = ""
user_1.info()

# Akses langsung atribut private dari luar
# try:
#     print(user_1.__username)
# except AttributeError as e:
#     print(f"\nError: {e}")
#     print("Attribut __username tidak bisa diakses langsung")

# Menggunakan getter untuk mwmbaaca data secara aman
# print("\n--- Mengakses data via Getter ---")
# nama_user = user_1.get_username()
# level_user = user_1.get_level()
# print(f"username dari getter: {nama_user}")
# print(f"level dari getter: {level_user}")

# menggunakan setter untuk mengubah data
print("\n--- Mencoba mengubah data via setter ---")
user_1.set_username("admin")
user_1.set_level("mode")
user_1.info()

print("\n--- Mencoba lagi dengan data yang valid ---")
user_1.set_username("Hollow Knight")
user_1.set_level("iridium")
user_1.info()