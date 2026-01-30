import pandas as pd
data = {
    'Nama': ['Alek', 'Arfy', 'Nino', 'Hijume', 'Yazuke'],
    'Prodi': ['Teknik Informatika', 'Sistem Informasi', 'Teknik Informatika', 'Sains Data', 'Pertanian'],
    'IPK': ['3.9', '3.6', '3.3', '3.5', '4.0'],
    'Semester': ['2', '2', '7', '5', '2'] 
}

df = pd.DataFrame(data)

print("--- Data Frame Mahasiswa --")
print(df)
