import yt_dlp

def download_yt_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'noplaylist': True,
        
        'outtmpl': '%(title)s.%(ext)s', 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Sedang mengunduh... mohon tunggu.")
            ydl.download([url])
        print("\n* Download Selesai!")
    except Exception as e:
        print(f"\n* Terjadi kesalahan: {e}")
        
if __name__ == "__main__":
    print("\n=== YOUTUBE DOWNLOADER ===\n")
    video_url = input("Masukkan URL video YouTube: ")
    download_yt_video(video_url)
