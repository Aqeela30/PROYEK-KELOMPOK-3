import tkinter as tk
from tkinter import messagebox, scrolledtext
import datetime


# Fungsi untuk menyimpan catatan
def simpan_catatan():
    tanggal = entry_tanggal.get()
    isi = text_catatan.get("1.0", tk.END).strip()
    if tanggal == "" or isi == "":
        messagebox.showwarning("Peringatan", "Tanggal dan isi catatan tidak boleh kosong.")
        return
    with open("catatan_harian.txt", "a") as file:
        file.write(f"{tanggal}: {isi}\n")
    messagebox.showinfo("Berhasil", "Catatan berhasil disimpan.")
    entry_tanggal.delete(0, tk.END)
    text_catatan.delete("1.0", tk.END)

# Fungsi untuk menampilkan catatan
def tampilkan_catatan():
    try:
        with open("catatan_harian.txt", "r") as file:
            isi = file.read()
    except FileNotFoundError:
        isi = "Belum ada catatan."

    window_catatan = tk.Toplevel(root)
    window_catatan.title("Daftar Catatan Harian")

    txt = scrolledtext.ScrolledText(window_catatan, width=50, height=20)
    txt.pack(padx=10, pady=10)
    txt.insert(tk.END, isi)
    txt.config(state='disabled')

# GUI Utama
root = tk.Tk()
root.title("📖 Catatan Harian")
root.geometry("400x400")

# Label Tanggal
label_tanggal = tk.Label(root, text="Tanggal (YYYY-MM-DD):")
label_tanggal.pack(pady=(10, 0))
entry_tanggal = tk.Entry(root, width=30)
entry_tanggal.pack()

# Auto isi tanggal hari ini
entry_tanggal.insert(0, datetime.date.today().isoformat())

# Label Catatan
label_catatan = tk.Label(root, text="Tulis catatan:")
label_catatan.pack(pady=(10, 0))

# Kotak teks catatan
text_catatan = tk.Text(root, width=45, height=10)
text_catatan.pack()

# Tombol simpan
btn_simpan = tk.Button(root, text="Simpan Catatan", command=simpan_catatan, bg="lightgreen")
btn_simpan.pack(pady=(10, 5))

# Tombol tampilkan
btn_lihat = tk.Button(root, text="Lihat Catatan", command=tampilkan_catatan, bg="lightblue")
btn_lihat.pack(pady=5)

# Tombol keluar
btn_keluar = tk.Button(root, text="Keluar", command=root.destroy, bg="salmon")
btn_keluar.pack(pady=(5, 10))

root.mainloop()