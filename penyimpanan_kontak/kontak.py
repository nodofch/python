daftar_kontak = {}


def tampilkan_menu():
    print("\n<-- Manajemen Kontak -->")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda (1-5): ")
    return pilihan


def tambah_kontak(daftar):
    nama = input("Masukkan Nama Kontak: ")
    nomor = input("Masukkan Nomor Telepon: ")

    daftar[nama] = nomor
    print(f"* Kontak '{nama}' berhasil ditambahkan. *")


def lihat_kontak(daftar):
    if not daftar:
        print("* Daftar kontak kosong. *")
        return

    print("\n<-- DAFTAR KONTAK -->")

    for nama, nomor in daftar.items():
        print(f"*Nama: {nama} | Nomor: {nomor} *")


def cari_kontak(daftar):
    nama = input("Masukkan Nama yang ingin dicari: ")

    if nama in daftar:
        print(f"* Kontak Ditemukan -> Nama: {nama} | Nomor: {daftar[nama]} *")
    else:
        print(f"* Kontak '{nama}' tidak ditemukan. *")


def main():
    daftar_kontak = {}

    while True:
        pilihan = tampilkan_menu()

        if pilihan == "1":
            tambah_kontak(daftar_kontak)
        elif pilihan == "2":
            lihat_kontak(daftar_kontak)
        elif pilihan == "3":
            cari_kontak(daftar_kontak)

        elif pilihan == "4":
            nama_hapus = input("Masukkan Nama Kontak yang akan dihapus: ")
            if nama_hapus in daftar_kontak:
                del daftar_kontak[nama_hapus]
                print(f"Kontak '{nama_hapus}' berhasil dihapus.")
            else:
                print(f"Kontak '{nama_hapus}' tidak ditemukan.")

        elif pilihan == "5":
            print("Terima kasih, program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
