import numpy as np

np.random.seed(42)
data_suhu = np.random.uniform(30, 80, (3, 7, 24))

print("== SERVER TEMPERATUR REPORT ==")
print(f"Bentuk Data (Server, Hari, Jam): {data_suhu.shape}")

rata_total = np.mean(data_suhu)
print(f"\nRata-rata suhu global: {rata_total:.2f}°C")

rata_per_server = np.mean(data_suhu, axis=(1, 2))
for i, rata in enumerate(rata_per_server):
    print(f"Server {i+1} avarage: {rata:.2f}°C")
    
overheat_limit = 75
panas_banget = data_suhu > overheat_limit

jumlah_overheat = np.sum(panas_banget)
print(f"\nTotal insiden overheat (>75°C): {jumlah_overheat} kali")

server_1_weekly = data_suhu[0].reshape(7, 24)
print(f"\nData Server 1 berhasil di-reshape ke format mingguan (7x24)")
avg_daily_s1 = np.mean(server_1_weekly, axis=1)
hari_terpanas = np.argmax(avg_daily_s1)
print(f"Server 1 paling panas pada hari ke-{hari_terpanas} (Indeks)")
