import sys
import time

DATABASE_AKUN = {}


def tampilkan_menu():
    """Menampilkan menu utama dan mengambil pilihan pengguna."""
    print("\n--- Sistem Login Akun Sederhana ---")
    print("1. Registrasi (Daftar Akun Baru)")
    print("2. Login (Masuk)")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan Anda (1-3): ")
    return pilihan


def registrasi(db):
    """
    Fungsi untuk mendaftarkan akun baru.
    Memeriksa ketersediaan username.
    """
    print("\n--- REGISTRASI AKUN ---")
    while True:
        username = input("Masukkan Username Baru: ")

        if username in db:
            print(f"Username '{username}' sudah terdaftar. Silakan coba username lain.")
        elif len(username) < 3:
            print("Username minimal harus 3 karakter.")
        else:
            break

    password = input("Masukkan Password: ")

    _show_loading("Mendaftarkan")

    db[username] = password
    print(f"\n✅ Akun '{username}' berhasil didaftarkan!")


def _show_loading(message="Memproses", dots=3, delay=0.25):
    """Tampilkan animasi loading sederhana dengan titik-titik."""
    print(f"{message}", end="", flush=True)
    for _ in range(dots):
        print(".", end="", flush=True)
        time.sleep(delay)
    print()


def login(db):
    """
    Fungsi untuk memproses login.
    Memeriksa username dan password.
    """
    print("\n--- LOGIN AKUN ---")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    _show_loading("Memverifikasi")

    if username in db:
    
        if db[username] == password:
            print(f"\n🎉 Selamat datang, {username}! Login berhasil.")
            return True
        else:
            print("\n❌ Password salah.")
            return False
    else:
        print("\n❌ Username tidak ditemukan. Silakan registrasi terlebih dahulu.")
        return False


def main():
    """Fungsi utama untuk menjalankan program."""

    while True:
        pilihan = tampilkan_menu()

        if pilihan == "1":
            registrasi(DATABASE_AKUN)
        elif pilihan == "2":
            status_login = login(DATABASE_AKUN)
            if status_login:
                pass
        elif pilihan == "3":
            _show_loading("Keluar")
            print("\nTerima kasih, program berakhir.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
