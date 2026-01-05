import random

def main():
    print("="*80)
    print("                            <-- GAME TEBAK ANGKA -->")
    print("="*80)

    #PILIH LEVEL
    angka_rahasia = 0
    while True:
        print(" ")
        print("\nPilih Level Kesuliatan")
        print("1. LOW (1-50)")
        print("2. HIGH (1-100)")
        print("3. EXTRIME (1-500)")
        pilih_level = input("Pilih sesuai angka [1,2,3]: ")

        if pilih_level == "1":
            angka_rahasia = random.randint(1, 50)
            break
        elif pilih_level == "2":
            angka_rahasia = random.randint(1, 100)
            break
        elif pilih_level == "3":
            angka_rahasia = random.randint(1, 500)
            break
        else:
            print("ERROR! Pilihan tidak tersedia. Masukkan angka 1, 2, atau 3.")

    #LOGIKA PERMAINAN
    max_tebakan = 7
    tebakan_benar = False
    while not tebakan_benar and max_tebakan > 0:
        try:
            print(" ")
            print(f"\tSisa nyawa: {max_tebakan}")
            tebakan = int(input("Masukkan angka tebakan anda: "))
            if tebakan > angka_rahasia:
                max_tebakan -= 1
                print(" ")
                print("Angka terlalu TINGGI! Masukkan angka yang lebih kecil.")
            elif tebakan < angka_rahasia:
                max_tebakan -= 1
                print(" ")
                print("Angka terlalu RENDAH! Masukkan angka yang lebih besar.")
            else:
                print(" ")
                print(f"\t!!! Selamat Anda berhasil menebak angka {angka_rahasia}. !!!")
                tebakan_benar = True
        except ValueError:
            print("ERROR! Masukkan angka bukan huruf.")

        #KALAH
    if max_tebakan == 0:
        print(" ")
        print("\n\t!! KALAH !!")
        print("YAHH SKILL ISSUE! Nyawa anda telah habis")
        print(f"Jawabannya adalah: {angka_rahasia}")

    print(" ")
    print("="*80)
    print("                         <-- GAME TELAH BERAKHIR -->")
    print("="*80)

if __name__ == "__main__":
    main()
            


