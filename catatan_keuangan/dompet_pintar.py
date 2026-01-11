import json
import os

FILENAME = "data_keuangan.json"

def muat_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {"saldo": 0, "riwayat": []}
        
    return {"saldo": 0, "riwayat": []}

def simpan_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def main():
    data = muat_data()

    if data is None:
        data = {"saldo": 0, "riwayat": []}

    while True:
        print("\n" + "-"*30)
        print(f"SALDO ANDA: Rp {data['saldo']}")
        print("-"*30)
        print("1. Tambah Pemasukan")
        print("2. Tambah pengeluaran")
        print("3. Lihat Riwayat")
        print("4. Keluar")

        pilih = input("Pilih Menu (1/2/3/4): ")

        try:
            if pilih == "1":
                nominal = int(input("Nominal Pemasukan: "))
                ket = input("Keterangan: ")

                data["saldo"] += nominal
                data["riwayat"].append({"tipe": "Masuk", "jumlah": nominal, "ket": ket})
                simpan_data(data)
                print("- Berhasil Dicatat! -")

            elif pilih == "2":
                nominal = int(input("Nominal Pengeluaran: "))
                if nominal > data["saldo"]:
                    print("- Saldo Tidak Cukup! -")
                else:
                    ket = input("Keterangan: ")
                    data["saldo"] -= nominal
                    data["riwayat"].append({"tipe": "Keluar", "jumlah": nominal, "ket": ket})
                    simpan_data(data)
                    print("- Berhasil Dicatat! -")
            
            elif pilih == "3":
                print("\nRiwayat Transaksi:")
                for item in data["riwayat"]:
                    simbol = "[+]" if item["tipe"] == "Masuk" else "[-]"
                    print(f"{simbol} Rp {item['jumlah']} | {item['ket']}")
            
            elif pilih == "4":
                print("Sampai Jumpa! Jangan Boros Yaa.")
                break
        
        except ValueError:
            print("- Tolong masukkan angka, bukan huruf! -")

if __name__ == "__main__":
    main()