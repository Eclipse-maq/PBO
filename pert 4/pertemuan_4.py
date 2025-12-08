class Character:
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        print(f"{self.__name} bergabung dalam pertarungan")

    def show_info(self):
        print("\n--- Character Info ---")
        print(f"Name\t: {self.__name}")
        print(f"Name\t: {self.__health}")
        print(f"Name\t: {self.__attack_power}")

    def attack(self, target):
        print(f"{self.__name} menyerang {target.get_name()}")
        target.take_damage(self.__attack_power)

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f"{self.__name} telah dikalahkan")
            self.__health = 0
        else:
            print(f"Health {self.__name} tersisa {self.__health}")

    def get_name(self):
        return self.__name
    
class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.__armor = armor
        print(f"Armor set to: {self.__armor}")

    def show_info(self):
        super().show_info()
        print(f"armor\t: {self.__armor}")

print("--- Membuat objek dari paretn class ---")
aragorn = Character("Aragorn", 100, 15)
aragorn.show_info()

print("\n--- membuat objek dari child class---")
gimli = Warrior("Gimli", 120, 20, 5)
gimli.show_info()

print("\n--- Pertarungan dimulai ---")
aragorn.attack(gimli)
gimli.attack(aragorn)

gimli.show_info()