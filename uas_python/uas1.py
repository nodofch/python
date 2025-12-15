# Program Tiket Bioskop Sederhana
usia = int(input("\nMasukkan usia Anda: "))
hari = input("Masukkan hari (senin -> minggu): ").lower()
jam_nonton = int(input("Masukkan jam mulai nonton (dalam format 24 jam): "))

print("\n<-- Hasil Pengrcekan Tiket -->")
if usia < 5 or usia > 60:
    print("Selamat Anda mendapat tiket GRATIS!!.")
    harga = 0
elif hari != "sabtu" and hari != "minggu" and hari != "jumat" and jam_nonton < 17:
    print("Tiket PROMO SIANG hari kerja.")
    harga = 25000
elif hari == "jumat" or hari == "sabtu" or hari == "minggu":
    print("Tiket HARGA AKHIR PEKAN/LIBUR")
    harga = 50000
else:
    print("Tiket HARGA NORMAL hari kerja.")
    harga = 35000

print(f"Harga tiket Anda adalah: Rp {harga:,}")
