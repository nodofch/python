import requests
import os

def ambil_kurs(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            idr_rate = data['conversion_rates']['IDR']
            eur_rate = data['conversion_rates']['EUR']
            jpy_rate = data['conversion_rates']['JPY']

            os.system('clear')
            print("=== REAL-TIME CURRENCY TRACKER ===")
            print(f"Update Terakhir: {data['time_last_update_utc']}")
            print("-" * 35)
            print(f"1 USD  =  Rp {idr_rate:,.2f}")
            print(f"1 USD  =  € {eur_rate:,.4f}")
            print(f"1 USD  =  ¥ {jpy_rate:,.2f}")

            print("\nSimulasi Konversi:")
            usd_input = float(input("Masukkan nominal USD: $"))
            print(f"Jika kamu punya ${usd_input}, nilainya: Rp {usd_input * idr_rate:,.2f}")

        else:
            print(f"Gagal mengambil data. Status: {data['result']}")

    except Exception as e:
        print(f"Terjadi Error: {e}")

if __name__ == "__main__":
    MY_API_KEY = "MASUKKAN API KEY KAMU"

    if MY_API_KEY == "MASUKKAN API KEY KAMU":
        print("Masukkan API Key kamu dulu didalam kode!")
    else:
        ambil_kurs(MY_API_KEY)



