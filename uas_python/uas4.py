angka_rahasia = 7
max_percobaan = 3
percobaan = 0

print("\n\t<-- Selamat Datang di Game Tebak Angka -->")
print(f"\nAnda memiliki {max_percobaan} kali kesempatan")

while True:
    percobaan += 1

    if percobaan > max_percobaan:
        print(f"\nKesempatan Anda telah habis! Angka rahasia adalah {angka_rahasia}.")
        break

    tebakan = int(input(f"Percobaan ke-{percobaan}: Masukkan tebakan Anda (1-10): "))
    if tebakan == angka_rahasia:
        print(f"\n* Selamat Anda berhasil menebak angka rahasia {angka_rahasia}! *")
        break

    elif tebakan < angka_rahasia:
        print("Tebakan terlalu kecil. Coba lagi!")

    else:
        print("Tebakan terlalu besar. Coba lagi!")
