import tkinter as tk
from tkinter import ttk, messagebox

class Antrenman:
    def __init__(self, ad, puan):
        self.ad = ad
        self.puan = puan

class Sporcu:
    def __init__(self, ad, spor_dali):
        self.ad = ad
        self.spor_dali = spor_dali
        self.antrenmanlar = []

    def antrenman_ekle(self, antrenman):
        self.antrenmanlar.append(antrenman)

    def rapor_al(self):
        if not self.antrenmanlar:
            return "Kayıtlı antrenman bulunamadı."
        rapor = f"📋 {self.ad} ({self.spor_dali}) Antrenman Raporu:\n\n"
        for a in self.antrenmanlar:
            rapor += f"- {a.ad} | Puan: {a.puan}\n"
        return rapor

class AntrenmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Antrenman Takip Sistemi")
        self.root.geometry("550x500")
        self.root.configure(bg="#e6f2ff")

        self.sporcular = []

        # Başlık
        ttk.Label(root, text="🏋️ Antrenman Takip Sistemi", font=("Segoe UI", 16, "bold")).pack(pady=10)

        # Form çerçevesi
        frame = ttk.Frame(root)
        frame.pack(pady=10)

        # Sporcu Adı
        ttk.Label(frame, text="Sporcu Adı:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.sporcu_ad_entry = ttk.Entry(frame, width=30)
        self.sporcu_ad_entry.grid(row=0, column=1, pady=5)

        # Spor Dalı
        ttk.Label(frame, text="Spor Dalı:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.spor_dal_entry = ttk.Entry(frame, width=30)
        self.spor_dal_entry.grid(row=1, column=1, pady=5)

        # Antrenman Adı
        ttk.Label(frame, text="Antrenman Adı:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.antrenman_ad_entry = ttk.Entry(frame, width=30)
        self.antrenman_ad_entry.grid(row=2, column=1, pady=5)

        # Puan
        ttk.Label(frame, text="Puan (0-100):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.puan_entry = ttk.Entry(frame, width=30)
        self.puan_entry.grid(row=3, column=1, pady=5)

        # Butonlar çerçevesi
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Sporcu ve Antrenman Ekle", command=self.sporcu_antrenman_ekle).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Rapor Al", command=self.rapor_goster).grid(row=0, column=1, padx=10)

        # Rapor alanı
        self.rapor_alan = tk.Text(root, height=15, width=65)
        self.rapor_alan.pack(pady=10)
        self.rapor_alan.configure(state="disabled", font=("Courier New", 10))

    def sporcu_antrenman_ekle(self):
        ad = self.sporcu_ad_entry.get().strip()
        dal = self.spor_dal_entry.get().strip()
        antrenman_ad = self.antrenman_ad_entry.get().strip()
        puan_str = self.puan_entry.get().strip()

        if not ad or not dal or not antrenman_ad or not puan_str:
            messagebox.showwarning("Hata", "Tüm alanları doldurun!")
            return

        try:
            puan = int(puan_str)
            if not (0 <= puan <= 100):
                raise ValueError
        except:
            messagebox.showwarning("Hata", "Puan 0 ile 100 arasında tam sayı olmalı!")
            return

        # Sporcu varsa bul yoksa oluştur
        sporcu = None
        for s in self.sporcular:
            if s.ad.lower() == ad.lower():
                sporcu = s
                break

        if not sporcu:
            sporcu = Sporcu(ad, dal)
            self.sporcular.append(sporcu)

        # Antrenmanı ekle
        sporcu.antrenman_ekle(Antrenman(antrenman_ad, puan))
        messagebox.showinfo("Başarılı", f"{ad} için '{antrenman_ad}' antrenmanı eklendi.")

        # Alanları temizle
        self.antrenman_ad_entry.delete(0, tk.END)
        self.puan_entry.delete(0, tk.END)

    def rapor_goster(self):
        self.rapor_alan.configure(state="normal")
        self.rapor_alan.delete(1.0, tk.END)
        if not self.sporcular:
            self.rapor_alan.insert(tk.END, "Henüz sporcu veya antrenman eklenmedi.")
        else:
            for s in self.sporcular:
                self.rapor_alan.insert(tk.END, s.rapor_al() + "\n")
        self.rapor_alan.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = AntrenmanApp(root)
    root.mainloop()
