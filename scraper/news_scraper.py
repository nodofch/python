import requests
from bs4 import BeautifulSoup

FILENAME = "data_keungan.json"

def main():
    url = "https://quotes.toscrape.com/"

    print(f"\n-- MEMULAI SCRAPING KE: {url} --\n")

    try:
        respons = requests.get(url)

        if respons.status_code == 200:
            soup = BeautifulSoup(respons.text, 'html.parser')

            kutipan = soup.find_all('span', class_='text')
            penulis = soup.find_all('small', class_='author')

            print(f"Berhasil mengambil {len(kutipan)} data\n")            

            for i in range(len(kutipan)):
                print(f"{i+1}. {kutipan[i].get_text()}")
                print(f"   Oleh: {penulis[i].get_text()}\n")

        else:
            print(f"Gagal Akses. Status code: {respons.status_code}")

    except Exception as e:
        print(f"Terjadi ERROR!: {e}")

if __name__ == "__main__":
    main()