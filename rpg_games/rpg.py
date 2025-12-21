import random
import time
import sys

def show_loading(seconds=3, message="Memproses"):
    # Simple loading animation that prints dots for the given duration
    print(f"{message}", end='', flush=True)
    interval = 0.5
    steps = max(1, int(seconds / interval))
    for _ in range(steps):
        time.sleep(interval)
        print('.', end='', flush=True)
    print()

class Monster:
    def __init__(self, nama, level, hp, atk, defense):
        self.nama = nama
        self.level = level
        self.max_hp = hp + (level * 10)
        self.hp = self.max_hp
        self.atk = atk + (level * 2)
        self.defense = defense + (level * 1)
        self.exp = 0
        self.next_level = 100
        # loot table: list of tuples (item_name or None, weight)
        self.loot = []
        self.is_defending = False

    def cek_status(self):
        print(f"\n[{self.nama} - Lvl {self.level}]")
        print(f"HP: {self.hp}/{self.max_hp} | ATK: {self.atk} | DEF: {self.defense}")

    def level_up(self):
        self.level += 1
        self.max_hp += 15
        self.hp = self.max_hp
        self.atk += 3
        self.defense += 2
        self.exp = 0
        self.next_level = int(self.next_level * 1.5)
        print(f"✨ {self.nama} NAIK KE LEVEL {self.level}! Statistik meningkat!")

    def drop_loot(self):
        """Return a random loot item (string) or None if nothing drops."""
        if not self.loot:
            return None
        items, weights = zip(*self.loot)
        choice = random.choices(items, weights=weights, k=1)[0]
        return choice if choice != "Nothing" else None

class Character:
    def __init__(self, nama, role, level, hp, atk, defense, skill_name):
        self.nama = nama
        self.role = role
        self.level = level
        self.max_hp = hp + (level * 10)
        self.hp = self.max_hp
        self.atk = atk + (level * 2)
        self.defense = defense + (level * 1)
        self.exp = 0
        self.next_level = 100
        self.skill_name = skill_name
        self.skill_ready = True
        self.temp_def_penalty = 0

    def cek_status(self):
        print(f"\n[{self.nama} - {self.role} - Lvl {self.level}]")
        print(f"HP: {self.hp}/{self.max_hp} | ATK: {self.atk} | DEF: {self.defense}")
        print(f"Skill: {self.skill_name} | Ready: {'Yes' if self.skill_ready else 'No'}")
        print(f"EXP: {self.exp}/{self.next_level}")

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.atk += 4
        self.defense += 2
        self.exp = 0
        self.next_level = int(self.next_level * 1.5)
        self.skill_ready = True
        print(f"✨ {self.nama} NAIK KE LEVEL {self.level}! Statistik meningkat!")

    def use_skill(self, enemy):
        if not self.skill_ready:
            print("⚠️ Skill belum siap!")
            return
        print(f"✨ Kamu menggunakan skill: {self.skill_name}!")
        if self.role == "Warrior":
            damage = max(0, (self.atk * 2) - enemy.defense)
            enemy.hp -= damage
            self.temp_def_penalty = 2
            print(f"⚔️ Berserk! {enemy.nama} terkena {damage} damage. (Def kamu turun sementara)")
        elif self.role == "Archer":
            damage = max(0, self.atk - (enemy.defense // 2))
            enemy.hp -= damage
            print(f"🏹 Piercing Shot! {enemy.nama} terkena {damage} damage (mengurangi pertahanan musuh).")
        elif self.role == "Healer":
            heal = 40 + (self.level * 5)
            self.hp = min(self.max_hp, self.hp + heal)
            print(f"💚 Divine Heal! Kamu memulihkan {heal} HP.")
        elif self.role == "Assassin":
            damage = max(0, (self.atk * 3) - enemy.defense)
            enemy.hp -= damage
            print(f"🗡️ Backstab! {enemy.nama} terkena {damage} damage (kritikal).")
        self.skill_ready = False


def pilih_karakter():
    print("\n=== PILIH KARAKTERMUKA ===")
    print("1. Wario  - Warrior (ATK Tinggi, DEF Tinggi)")
    print("2. Arhano - Archer  (ATK Tinggi, DEF Rendah, skill tembakan pierce)")
    print("3. Raffael- Healer  (Menyembuhkan dengan skill)")
    print("4. Assassiono - Assassin (Serangan kritikal tinggi)")
    pilihan = input("Pilih (1/2/3/4): ")
    show_loading(3, "Memilih karakter...")

    if pilihan == "1":
        return Character("Wario", "Warrior", 1, 120, 12, 8, "Berserk")
    elif pilihan == "2":
        return Character("Arhano", "Archer", 1, 90, 14, 5, "Piercing Shot")
    elif pilihan == "3":
        return Character("Raffael", "Healer", 1, 100, 8, 6, "Divine Heal")
    else:
        return Character("Assassiono", "Assassin", 1, 80, 16, 4, "Backstab")
    
def cari_lawan(player_level):
    daftar = ["Slime", "Goblin", "Bat", "Rat", "Orc", "Troll", "Wolf", "Skeleton", "Mage"]
    nama_musuh = random.choice(daftar)
    level_musuh = random.randint(1, max(1, player_level)) # Level tidak akan melebihi player

    if nama_musuh == "Slime":
        m = Monster("Slime", level_musuh, 60, 6, 6)
        m.loot = [("Slime Gel", 50), ("Gold Coin", 40), ("Nothing", 10)]
        return m
    elif nama_musuh == "Goblin":
        m = Monster("Goblin", level_musuh, 40, 10, 3)
        m.loot = [("Rusty Dagger", 30), ("Gold Coin", 50), ("Goblin Ear", 20)]
        return m
    elif nama_musuh == "Bat":
        m = Monster("Bat", level_musuh, 25, 5, 2)
        m.loot = [("Bat Wing", 40), ("Gold Coin", 50), ("Nothing", 10)]
        return m
    elif nama_musuh == "Rat":
        m = Monster("Rat", level_musuh, 20, 4, 1)
        m.loot = [("Rat Tail", 40), ("Gold Coin", 50), ("Nothing", 10)]
        return m
    elif nama_musuh == "Orc":
        m = Monster("Orc", level_musuh, 80, 14, 6)
        m.loot = [("Orc Tooth", 35), ("Iron Ore", 40), ("Gold Coin", 25)]
        return m
    elif nama_musuh == "Troll":
        m = Monster("Troll", level_musuh, 120, 10, 10)
        m.loot = [("Troll Hide", 40), ("Large Bone", 30), ("Gold Coin", 30)]
        return m
    elif nama_musuh == "Wolf":
        m = Monster("Wolf", level_musuh, 50, 12, 4)
        m.loot = [("Wolf Fang", 45), ("Gold Coin", 45), ("Nothing", 10)]
        return m
    elif nama_musuh == "Skeleton":
        m = Monster("Skeleton", level_musuh, 60, 9, 5)
        m.loot = [("Bone", 50), ("Old Sword", 20), ("Gold Coin", 30)]
        return m
    else:
        m = Monster("Mage", level_musuh, 45, 16, 3)
        m.loot = [("Magic Dust", 40), ("Gold Coin", 40), ("Mystic Tome", 20)]
        return m

def battle(player, enemy, inventory):
    print(f"\n💥 Pertarungan Dimulai: {player.nama} ({player.role}) vs {enemy.nama} (Lvl {enemy.level})")

    while player.hp > 0 and enemy.hp > 0:
        player.cek_status()
        print(f"HP Musuh ({enemy.nama}): {enemy.hp}")
        print("\n--- GILIRANMU ---")
        print("1. Attack  2. Defend  3. Skill  4. Run  5. Use Potion  6. Inspect Enemy")
        aksi = input("Pilih aksi: ")
        show_loading(3, "Memproses aksi...")
        is_defending = False

        # --- GILIRAN PLAYER ---
        if aksi == "1": # ATTACK
            # consider if enemy was defending
            enemy_def = enemy.defense * 2 if getattr(enemy, 'is_defending', False) else enemy.defense
            damage = max(0, player.atk - enemy_def)
            enemy.hp -= damage
            # attacking breaks enemy defend stance
            enemy.is_defending = False
            print(f"⚔️ Kamu menyerang {enemy.nama} sebesar {damage} damage!")
        elif aksi == "2": # DEFEND
            print("🛡️ Kamu bersiap bertahan! (Damage musuh berkurang)")
            is_defending = True
        elif aksi == "3": # SKILL
            player.use_skill(enemy)
        elif aksi == "4": # RUN
            if random.random() > 0.5:
                print("🏃 Kamu berhasil kabur!")
                return "kabur"
            else:
                print("❌ Gagal kabur!")
        elif aksi == "5": # POTION
            if inventory.get("Potion", 0) > 0:
                heal_amount = 30
                player.hp = min(player.max_hp, player.hp + heal_amount)
                inventory["Potion"] -= 1
                print(f"🧪 Kamu minum Potion dan memulihkan {heal_amount} HP!")
            else:
                print("⚠️ Tidak ada Potion di inventory!")

        if enemy.hp <= 0:
            print(f"🏆 {enemy.nama} kalah!")
            # Reward EXP
            gained_exp = 50 * enemy.level
            player.exp += gained_exp
            print(f"✨ Kamu mendapatkan {gained_exp} EXP!")

            # Loot drop
            loot = enemy.drop_loot()
            if loot:
                inventory[loot] = inventory.get(loot, 0) + 1
                print(f"🎁 Loot: Kamu mendapat '{loot}'!")
            else:
                print("🎁 Loot: Tidak ada item yang didapat.")

            # Immediate level up per permintaan
            print("⭐ Karena mengalahkan musuh, kamu naik 1 level!")
            player.level_up()

            # Also check EXP-based level-up (if reached)
            if player.exp >= player.next_level:
                player.level_up()

            return "menang"

        # --- GILIRAN MUSUH ---
        print(f"\n--- GILIRAN {enemy.nama} ---")
        # Musuh memutuskan tindakan: attack / defend / skill
        show_loading(3, f"{enemy.nama} sedang bertindak...")
        enemy_action = random.choices(["attack", "defend", "skill"], weights=[70,20,10], k=1)[0]

        if enemy_action == "attack":
            effective_def = max(0, player.defense - player.temp_def_penalty)
            if is_defending:
                effective_def = effective_def * 2
            dmg_musuh = max(0, enemy.atk - effective_def)
            player.hp -= dmg_musuh
            print(f"🔥 {enemy.nama} menyerangmu sebesar {dmg_musuh} damage!")
        elif enemy_action == "defend":
            enemy.is_defending = True
            print(f"🛡️ {enemy.nama} bersiap bertahan! (Pertahanan musuh meningkat untuk giliran berikutnya)")
        else:  # skill
            effective_def = max(0, player.defense - player.temp_def_penalty)
            skill_dmg = max(0, int((enemy.atk * 2) - effective_def))
            player.hp -= skill_dmg
            print(f"✨ {enemy.nama} menggunakan skill spesial dan memberikan {skill_dmg} damage!")

        # reset temp penalties
        player.temp_def_penalty = 0

        if player.hp <= 0:
            print("💀 Kamu kalah... Game Over.")
            return "kalah"
        
def main():
    player = pilih_karakter()
    inventory = {"Potion": 3}

    while True:
        print("\n======== MENU UTAMA ========")
        print(f"Character: {player.nama} ({player.role}) | Level: {player.level}")
        print("1. Cari Lawan")
        print("2. Lihat Status & Inventory")
        print("3. Keluar Game")
        menu = input("Pilih menu: ")
        show_loading(3, "Memproses pilihan...")

        if menu == "1":
            player.skill_ready = True  # reset skill availability each encounter
            musuh = cari_lawan(player.level)
            hasil = battle(player, musuh, inventory)
            if hasil == "kalah": break
            player.hp = player.max_hp # Reset HP setelah battle agar bisa lanjut
        elif menu == "2":
            player.cek_status()
            print(f"Inventory: {inventory}")
        elif menu == "3":
            print("Terima kasih sudah bermain!")
            break

if __name__ == "__main__":
    main()