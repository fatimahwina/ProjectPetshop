import tkinter as tk
from tkinter import ttk
import pandas as pd

def load_csv(daftar_produk_path, data_produk_path):
    try:
        # Membaca file Daftar_Produk.csv
        daftar_df = pd.read_csv(daftar_produk_path)
        if 'No' not in daftar_df.columns:
            raise ValueError("Kolom 'No' tidak ditemukan di Daftar_Produk.csv")
        
        # Mengambil nomor dari 1-10
        nomor_list = daftar_df['No'].tolist()[:10]
        
        # Membaca file data_produk.csv
        data_df = pd.read_csv(data_produk_path)
        if 'No' not in data_df.columns:
            raise ValueError("Kolom 'No' tidak ditemukan di data_produk.csv")
        
        # Memfilter data berdasarkan nomor yang diambil
        filtered_df = data_df[data_df['No'].isin(nomor_list)]
        
        show_data(filtered_df)
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def show_data(df):
    # Menghancurkan treeview lama jika ada
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Membuat treeview
    tree = ttk.Treeview(frame)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    
    # Menambahkan header ke treeview
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    # Menambahkan data ke treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack(expand=True, fill="both")

# Membuat instance Tkinter
root = tk.Tk()
root.title("CSV Viewer")

# Membuat frame untuk menampilkan data
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

# Path ke file CSV
daftar_produk_path = r'C:\Praktikum prokom\ProjectPetshop\data\Daftar_Produk.csv'
data_produk_path = r'C:\Praktikum prokom\ProjectPetshop\data\data_produk.csv'

# Membuat tombol untuk memuat file CSV
btn_load = tk.Button(root, text="Load data", command=lambda: load_csv(daftar_produk_path, daftar_produk_path))
btn_load.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.geometry("800x600")
root.mainloop()
