import random
tinggi_daun = 9
tinggi_batang = 3

#WARNA
merah = "\033[91m"
hijau = "\033[92m"
kuning = "\033[93m"
tutup = "\033[0m"

POLA_DAUN = ["^", "^", "^", "o"]

for i in range(tinggi_daun):
    spasi = " " * (tinggi_daun - i)
    
    #Bintang paling atas
    if i == 0:
        print(f"{spasi}{kuning}*{tutup}")
    else:
        baris_daun = []
        for k in range(2 * i + 1):
            pola_sekarang = random.choice(POLA_DAUN)

            if pola_sekarang == "^":
                baris_daun.append(str(hijau)+"^"+str(tutup))
            else:
                baris_daun.append(str(merah)+"o"+str(tutup))
        print(spasi + "".join(baris_daun))

for j in range(tinggi_batang):
    spasi = " " * (tinggi_daun - 1)
    batang = "| |"
    print(spasi + batang)
