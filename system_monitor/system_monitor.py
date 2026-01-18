import psutil
import os
import time
from datetime import datetime


def format_bytes(n):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024


def cek_status():
    while True:
        os.system("clear")

        print("<== ARCH LIMUX SYSTEM MONITOR ==>")
        print(f"Waktu: {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 50)

        # CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Penggunaan CPU     : {cpu_usage}")

        # RAM
        mem = psutil.virtual_memory()
        print(
            f"Penggunaan RAM     : {mem.percent}% ({format_bytes(mem.used)} / {format_bytes(mem.total)})"
        )

        # DISK
        disk = psutil.disk_usage("/")
        print(
            f"Penyimpanan (/)    : {disk.percent}% ({format_bytes(disk.used)} / {format_bytes(disk.total)})"
        )

        # ALERT
        if cpu_usage > 80:
            print("\nPERINGATAN: Penggunaan CPU terlalu tinggi!")
        if mem.percent > 90:
            print("\nPERINGATAN: Penggunaan RAM hampir habis!")

        print("-" * 50)
        print("Tekan Ctrl+C untuk berhenti.")

        # jeda 2 detik
        time.sleep(3)


if __name__ == "__main__":
    try:
        cek_status()
    except KeyboardInterrupt:
        print("~ Monitoring Dihentikan! Sampai Jumpa ~")

