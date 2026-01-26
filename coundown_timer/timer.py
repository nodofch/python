import customtkinter as ctk
import time
import threading

class TimerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x250")
        self.title("Input Timer")

        self.label_instruksi = ctk.CTkLabel(self, text="Masukkan Detik:")
        self.label_instruksi.pack(pady=10)

        self.input_detik = ctk.CTkEntry(self, placeholder_text="Contoh: 60")
        self.input_detik.pack(pady=5)

        self.label_timer = ctk.CTkLabel(self, text="00:00", font=("Roboto", 40, "bold"))
        self.label_timer.pack(pady=20)

        self.btn_start = ctk.CTkButton(self, text="Mulai Timer", command=self.mulai_thread)
        self.btn_start.pack(pady=10)

    def mulai_thread(self):
        try:
            durasi = int(self.input_detik.get())
            threading.Thread(target=self.jalankan_timer, args=(durasi,), daemon=True).start()
        except ValueError:
            self.label_timer.configure(text="Error!")

    def jalankan_timer(self, detik):
        while detik >= 0:
            mins, secs = divmod(detik, 60)
            self.label_timer.configure(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            detik -= 1
        self.label_timer.configure(text="Selesai!")

if __name__ == "__main__":
    app = TimerGUI()
    app.mainloop()
