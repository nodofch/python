print("\n\t<-- Program Penghitung rata-rata Nilai -->")
jumlah_mapel = int(input("\nMasukkan jumlah mata pelajaran yang akan dihitung: "))
total_nilai = 0

print(" ")
print("-" * 40)

for i in range(1, jumlah_mapel + 1):
    nilai = float(input(f"Masukkan nilai mata pelajaran ke-{i}: "))
    total_nilai += nilai

if jumlah_mapel > 0:
    rata_rata = total_nilai / jumlah_mapel
    print("-" * 40)
    print(" ")
    print(f"Total nilai dari {jumlah_mapel} mapel: {total_nilai}")
    print(f"Rata-rata Nilai Anda adalah: {rata_rata:.2f}")
    print("\n\t<-- Program Selesai -->")
else:
    print("Tidak ada mata pelajaran yang dimasukkan")
