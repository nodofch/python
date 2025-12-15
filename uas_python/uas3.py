kapasitas_tangki = 30
print("\n\t<-- Program Isi Bensin -->")
bensin_saat_ini = float(input("\nMasukkan jumlah bensin saat ini (Liter): "))

print(f"\nkapasitas tangki maksimal: {kapasitas_tangki} Liter")

while bensin_saat_ini < kapasitas_tangki:
    print(f"\nBensin saat ini: {bensin_saat_ini:.2f} Liter")

    sisa_isi = kapasitas_tangki - bensin_saat_ini
    print(f"Anda bisa mengisi maksimal {sisa_isi:.2f} Liter lagi.")

    isi_tambahan = float(input("Berapa liter yang ingin anda isi sekarang?: "))

    if isi_tambahan <= 0:
        print("Jumlah isi harus lebih dari nol.")
        continue
    elif bensin_saat_ini + isi_tambahan <= kapasitas_tangki:
        bensin_saat_ini += isi_tambahan
        print(f"Berhasil diisi! Total bensin sekarang: {bensin_saat_ini:.2f} Liter")
    else:
        print("Jumlah yang anda masukkan MELEBIHI kapasitas tangki")

print("\n<-- TANGKI PENUH ATAU SUDAH CUKUP -->")
print(f"Pengisian selesai. Total bensin akhir: {bensin_saat_ini:.2f} Liter.")
