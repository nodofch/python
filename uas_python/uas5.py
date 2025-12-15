password_benar = "rahasia123"
max_login_percobaan = 3
status_login = False

print("\n\t<-- SISTEM LOGIN -->")
print(f"\nAnda memiliki kesempatan {max_login_percobaan} kali untuk login.")

for percobaan in range(1, max_login_percobaan + 1):
    kata_sandi = input(f"Percobaan ke-{percobaan}. Masukkan Kata Sandi: ")
    if kata_sandi == password_benar:
        print("\n\t<-- LOGIN BERHASIL -->")
        print("\n* Selamat Datang! *")
        status_login = True
        break

    elif percobaan < max_login_percobaan:
        print("Kata Sandi anda salah! Silahkan coba lagi.")

    else:
        print("\nKesempatan Anda habis!")
        print("Kata sandi salah! akun TERKUNCI sementara.")

if status_login:
    print("Akses ke dashboard diberikan.")
else:
    print("Akses Ditolak.")
