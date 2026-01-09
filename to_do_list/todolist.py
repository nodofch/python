import os

FILENAME = "inventory.txt"

def muat_inventory():
    #fungsi untuk mengambi data inventory.txt ke dalam list
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            daftar_inventory = [line.strip() for line in file.readlines()]
        return daftar_inventory

def simpan_inventory(daftar_inventory):
    with open(FILENAME, "w") as file:
        for inventory in daftar_inventory:
            file.write(inventory + "\n")

def main():
    inventory_list = muat_inventory()

    while True:
        print("\n" + "="*30)
        print("     TO-DO LIST GW     ")
        print("="*30)
        print("1. Lihat Inventory")
        print("2. Tambah Inventory")
        print("3. Hapus Inventory")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1/2/3/4): ")

        if pilihan == "1":
            print("\nDAFTAR INVENTORY ANDA")
            if not inventory_list:
                print("- Belum Ada data yang anda tambahkan di Inventory -")
            else:
                for i, inventory in enumerate(inventory_list, 1):
                    print(f"{i}. {inventory}")

        elif pilihan == "2":
            inventory_baru = input("Masukkan data yang ingin dimasukkan: ")
            inventory_list.append(inventory_baru)
            simpan_inventory(inventory_list)
            print("Data Berhasil Ditambahkan!")

        elif pilihan == "3":
            if not inventory_list:
                print("Tidak ada tugas yang dihapus.")
                continue

            for i, inventory in enumerate(inventory_list, 1):
                print(f"{i}. {inventory}")

            try:
                nomor = int(input("Masukkan nomor data yang ingin anda hapus: "))
                if 1 <= nomor <= len(inventory_list):
                    terhapus = inventory_list.pop(nomor - 1)
                    simpan_inventory(inventory_list)
                    print(f"Data '{terhapus}' berhasil terhapus.")
                else:
                    print("Nomor tidak valid!")
            except ValueError:
                print("Error! Masukkan angka.")

        elif pilihan == "4":
            print("Sampai Jumpa!")
            break
        else:
            print("Pilihan salah.")
            
if __name__ == "__main__":
    main()
            

