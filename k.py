import email
from tkinter import *
from tkinter import messagebox, Toplevel, Canvas, Button, PhotoImage, scrolledtext, simpledialog
import csv
from pathlib import Path
import shortcut_pandas as ps
import tkinter as tk
import pandas as pd
import datetime
import smtplib
import random
import datetime
import pandas as pd
import shortcut_pandas as ps
from fpdf import FPDF
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import google.generativeai as genai
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import datetime
import string

# Function to validate email format
def email_form(email):
    print(f"Validating email: {email}")  # Debugging
    is_valid = "@" in email and "." in email
    print(f"Email valid: {is_valid}")  # Debugging
    return is_valid

# Function to handle login
def login():
    global email_user
    username = username_entry.get()
    password = password_entry.get()
    sukses = False
    try:
        with open('data/login.csv', 'r') as file:  # Fixed the file path
            reader = csv.reader(file)
            for row in reader:
                a, b, c = row
                print("Checking:", a, b)
                if username == a and password == b:
                    sukses = True
                    break
    except FileNotFoundError as e:
        messagebox.showerror(title="Error", message=f"File not found: {e}")
        return
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
        return

    if sukses:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.withdraw()  # Hide the login window
        email_user = ps.get_email_by_username(username)
        halaman_menu()
    else:
        print("=" * 50)
        print("Username atau Password yang anda masukkan salah")
        print("=" * 50)
        messagebox.showerror(title="Error", message="Invalid login.")


def signup():
    name = username.get()
    password = user_password.get()
    email = user_email.get()

    print(f"Username: {name}, Password: {password}, Email: {email}")  # Debugging

    # Check if the username already exists
    try:
        with open('data/login.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == name:
                    messagebox.showerror(title="Error", message="Username sudah terdaftar, silakan pilih username lain.")
                    return
    except FileNotFoundError:
        # File not found means no users registered yet, so we can skip this check
        pass

    if email_form(email):
        try:
            kode_otp = ps.generate_otp()
            print(f"OTP generated: {kode_otp}")  # Debugging
            ps.send_otp_email(email, kode_otp)
            print("OTP sent to email")  # Debugging

            # Membuat Toplevel window untuk input OTP
            otp_window = Toplevel()
            otp_window.title("Enter OTP")
            otp_window.geometry("300x150")
            otp_window.configure(bg="Pink")
            otp_window.resizable(False, False)

            otp_label = Label(otp_window, text="Masukkan kode OTP:", font=("Arial", 12))
            otp_label.pack(pady=10)

            otp_entry = Entry(otp_window, width=20, font=("Arial", 12))
            otp_entry.pack()

            def verify_otp():
                verif = otp_entry.get()
                if verif == kode_otp:
                    try:
                        with open('data/login.csv', 'a', newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow([name, password, email])
                        messagebox.showinfo(title="Success", message="Register berhasil, silakan login")
                        otp_window.destroy()
                    except Exception as e:
                        messagebox.showerror(title="Error", message=f"An error occurred while saving data: {e}")
                else:
                    messagebox.showerror(title="Error", message="Kode OTP tidak valid, silahkan input dengan benar!")

            verify_button = Button(otp_window, text="Verify", command=verify_otp, width=10)
            verify_button.pack(pady=10)
        except Exception as e:
            print("An error occurred:", e)
            messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    else:
        messagebox.showerror(title="Error", message="Email tidak valid")


def halaman_login():
    global window, username_entry, password_entry
    
    window = Tk()
    window.geometry("1166x718")
    window.configure(bg="#ACCDFF")

    canvas = Canvas(
        window,
        bg="#ACCDFF",
        height=718,
        width=1166,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    window.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(583.0, 359.0, image=window.image_image_1)

    window.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(837.0, 368.0, image=window.image_image_2)

    canvas.create_text(
        696.0, 269.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Inter", 16 * -1))

    canvas.create_text(
        741.0, 193.0,
        anchor="nw",
        text="Sign in",
        fill="#FF27A8",
        font=("kavoon regular", 40 * -1))

    canvas.create_text(
        696.0, 348.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 16 * -1))

    window.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(298.0, 343.0, image=window.image_image_3)

    canvas.create_text(
        817.0, 487.0,
        anchor="nw",
        text="or",
        fill="#000000",
        font=("Inter", 16 * -1))

    window.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(838.0, 321.0, image=window.entry_image_1)

    username_entry = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0)
    username_entry.place(
        x=707.0, y=299.0,
        width=262.0, height=42.0)

    window.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(838.0, 399.0, image=window.entry_image_2)

    password_entry = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*")
    password_entry.place(
        x=707.0, y=377.0,
        width=262.0, height=42.0)

    window.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    Button(
        image=window.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_register,
        relief="flat").place(x=691.0, y=508.0, width=294.0, height=44.0)

    window.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    Button(
        image=window.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat").place(
        x=691.0, y=443.0,
        width=294.0, height=44.0)

    window.resizable(False, False)
    window.mainloop()

def halaman_register():
    global username, user_password, user_email, reg_window

    reg_window = Toplevel(window)
    reg_window.geometry("1166x718")
    reg_window.configure(bg="#ACCDFF")

    canvas = Canvas(reg_window, bg="#ACCDFF", height=718, width=1166, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    
    reg_window.image_image_1 = PhotoImage(file=relative_to_assets("image_a.png"))
    canvas.create_image(583.0, 359.0, image=reg_window.image_image_1)

    reg_window.image_image_2 = PhotoImage(file=relative_to_assets("image_b.png"))
    canvas.create_image(837.0, 368.0, image=reg_window.image_image_2)

    reg_window.entry_image_1 = PhotoImage(file=relative_to_assets("entry_a.png"))
    canvas.create_image(838.0, 465.0, image=reg_window.entry_image_1)
    user_email = Entry(reg_window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    user_email.place(
        x=707.0, y=443.0,
        width=262.0, height=42.0)

    canvas.create_text(696.0, 257.0, anchor="nw", text="Username", fill="#000000", font=("Inter", 16 * -1))

    canvas.create_text(741.0, 193.0, anchor="nw", text="Register", fill="#FF27A8", font=("Kavoon Regular", 40 * -1))
    
    reg_window.button_image_1 = PhotoImage(file=relative_to_assets("button_a.png"))
    tk.Button(
        reg_window,
        image=reg_window.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back_login,  # Pastikan fungsi back_menu sudah didefinisikan
        relief="flat",
        bg='#FFFFFF',  # Atur background sama dengan latar belakang window
        activebackground='#FFFFFF').place(
        x=640.0, y=180.0, 
        width=60.0, height=44.0)

    reg_window.button_image_2 = PhotoImage(file=relative_to_assets("button_b.png"))
    Button(
        reg_window, 
        image=reg_window.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=signup,
        relief="flat"
    ).place(
        x=691.0, y=508.0,
        width=294.0, height=44.0)

    canvas.create_text(
        696.0, 348.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 16 * -1))

    canvas.create_text(
        696.0, 414.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inter", 16 * -1))

    reg_window.image_image_3 = PhotoImage(file=relative_to_assets("image_c.png"))
    canvas.create_image(298.0, 343.0, image=reg_window.image_image_3)

    reg_window.entry_image_2 = PhotoImage(file=relative_to_assets("entry_b.png"))
    canvas.create_image(838.0, 308.0, image=reg_window.entry_image_2)
    username = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0)
    
    username.place(
        x=707.0, y=286.0,
        width=262.0, height=42.0)

    reg_window.entry_image_3 = PhotoImage(file=relative_to_assets("entry_c.png"))
    canvas.create_image(838.0, 387.0, image=reg_window.entry_image_3)
    user_password = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*")
    user_password.place(
        x=707.0, y=365.0,
        width=262.0, height=42.0)
    
    reg_window.button_image_2 = PhotoImage(file=relative_to_assets("button_b.png"))
    Button(
        reg_window, image=reg_window.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=signup,
        relief="flat").place(
        x=691.0, y=508.0,
        width=294.0, height=44.0)

    reg_window.resizable(False, False)
    reg_window.mainloop()

def halaman_menu():
    global window, menu_window
    menu_window = Toplevel(window)
    menu_window.geometry("1166x718")
    menu_window.configure(bg="#ACCDFF")

    canvas = Canvas(
        menu_window,
        bg="#FFFFFF",
        height=718,
        width=1146,
        bd=0,
        highlightthickness=0,
        relief="ridge")

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        169.0,
        1146.0,
        1283.0,
        fill="#FFFFFF",
        outline="")

    image_pawpaw = PhotoImage(
        file=relative_to_assets("pawpaw.png"))
    pawpaw = canvas.create_image(
        583.0,
        100.0,
        image=image_pawpaw)

    image_image_v = PhotoImage(file=relative_to_assets("image_v.png"))
    image_1 = canvas.create_image(807.0, 523.0, image=image_image_v)

    image_image_w = PhotoImage(file=relative_to_assets("image_w.png"))
    image_w = canvas.create_image(575.0, 272.0, image=image_image_w)

    image_image_x = PhotoImage(file=relative_to_assets("image_x.png"))
    image_x = canvas.create_image(250.0, 272.0, image=image_image_x)

    image_image_y = PhotoImage(file=relative_to_assets("image_y.png"))
    image_y = canvas.create_image(574.0, 102.0, image=image_image_y)

    canvas.create_text(450.0, 80.0, anchor="nw", text="Pilihan Menu", fill="#FFFFFF", font=("Candy Beans", 48 * -1))

    image_image_z = PhotoImage(file=relative_to_assets("image_z.png"))
    image_z = canvas.create_image(904.0, 267.0, image=image_image_z)

    image_image_i = PhotoImage(file=relative_to_assets("image_i.png"))
    image_i = canvas.create_image(406.0, 513.0, image=image_image_i)

    button_image_v = PhotoImage(file=relative_to_assets("button_v.png"))
    button_v = Button(
        menu_window,  # Make sure to specify the parent window
        image=button_image_v,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_beli_peralatan,
        relief="flat")
    button_v.image = button_image_v  # Keep a reference to the image
    button_v.place(
        x=469.0,
        y=362.0,
        width=207.0,
        height=40.0)

    button_image_w = PhotoImage(file=relative_to_assets("button_w.png"))
    button_w = Button(
        menu_window,
        image=button_image_w,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_layanan,
        relief="flat")
    button_w.image = button_image_w  # Keep a reference to the image
    button_w.place(
        x=800.0,
        y=362.0,
        width=207.0,
        height=40.0)

    button_image_x = PhotoImage(file=relative_to_assets("button_x.png"))
    button_x = Button(
        menu_window,
        image=button_image_x,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_printout,
        relief="flat")
    button_x.image = button_image_x  # Keep a reference to the image
    button_x.place(
        x=302.0,
        y=619.0,
        width=207.0,
        height=40.0)

    button_image_y = PhotoImage(file=relative_to_assets("button_y.png"))
    button_y = Button(
        menu_window,
        image=button_image_y,
        borderwidth=0,
        highlightthickness=0,
        command=keluar, relief="flat")
    button_y.image = button_image_y  # Keep a reference to the image
    button_y.place(
        x=708.0,
        y=619.0,
        width=207.0,
        height=40.0)

    button_image_z = PhotoImage(file=relative_to_assets("button_z.png"))
    button_z = Button(
        menu_window,
        image=button_image_z,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_beli_makan,
        relief="flat")
    button_z.image = button_image_z  # Keep a reference to the image
    button_z.place(
        x=125.0,
        y=362.0,
        width=246.0,
        height=35.0)

    menu_window.resizable(False, False)
    menu_window.mainloop()

produk_df = pd.read_csv('data/Daftar_Produk.csv')

def keluar():
    messagebox.showinfo("Terima Kasih", "Terima kasih telah menggunakan program ini.")
    menu_window.withdraw()
    window.deiconify()
    window.focus_force()


def print_produk(username_entry):
    username = username_entry.get()  # Ambil username dari input entry
    if not username:
        messagebox.showerror("Error", "Harap masukkan username")
        return
    
    email_user = ps.get_email_by_username(username)  # Mengambil email berdasarkan username
    if email_user:
        pdf_filename = ps.generate_transaction_pdf(email_user)
        if pdf_filename:
            ps.send_email_with_pdf(email_user, pdf_filename)
    else:
        messagebox.showerror("Error", "Username tidak ditemukan")

def print_layanan(username_entry):
    username = username_entry.get()  # Ambil username dari input entry
    if not username:
        messagebox.showerror("Error", "Harap masukkan username")
        return
    
    email_user = ps.get_email_by_username(username)  # Mengambil email berdasarkan username
    if email_user:
        pdf_filename = ps.generate_layanan_pdf(email_user)
        if pdf_filename:
            ps.send_layanan_with_pdf(email_user, pdf_filename)
    else:
        messagebox.showerror("Error", "Username tidak ditemukan")

def halaman_printout():
    root = tk.Tk()
    root.title("Print Options")

    # Membuat frame untuk input username
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Membuat tombol untuk print produk
    print_produk_button = tk.Button(root, text="Print Produk", command=lambda: print_produk(username_entry))
    print_produk_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Membuat tombol untuk print layanan
    print_layanan_button = tk.Button(root, text="Print Layanan", command=lambda: print_layanan(username_entry))
    print_layanan_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Menjalankan loop utama tkinter
    root.mainloop()

produk_dp = pd.read_csv('data/Daftar_Peralatan.csv')

def kirim_email(recipient, subject, body):
    sender_email = "petshopkiwkiw@gmail.com"
    sender_password = "huna bhnh uinc zpgb"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def buat_otp():
    otp = ''.join(random.choices(string.ascii_letters, k=5))
    return otp

def send_email(recipient, subject, body):
    sender_email = "petshopkiwkiw@gmail.com"
    sender_password = "huna bhnh uinc zpgb"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def generate_otp():
    otp = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    return otp

def struk_beli_peralatan(name, email_address, current_time, total, otp, cart):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "petshopkiwkiw@gmail.com"
    smtp_password = "huna bhnh uinc zpgb"

    item_details = "\n".join([f"- {item['Nama Peralatan']}: Rp{item['Harga']:,}" for item in cart])

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email_address
    msg['Subject'] = "Invoice Pembayaran Pembelian Peralatan KiwKiw Petshop"

    body = f"""
==================================================
                RINCIAN PEMBELIAN
==================================================

  Nama                    : {name}
  Waktu pemesanan         : {current_time}
  Total Harga             : Rp {total:,}
  Otp                     : {otp}

  Detail Pembelian:
  {item_details}

==================================================
TERIMA KASIH {name} TELAH BERBELANJA DI KIWKIW PETSHOP
==================================================
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("----Email dengan invoice Pembelian Peralatan telah berhasil dikirim ke email anda!----")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

# Fungsi Konfirmasi Pembayaran
def confirm_payment():
    global email_address, cart, total, current_time
    username = username_entry.get()
    jenis_layanan = "Pembelian Peralatan"
    detail_window.destroy()
    proceed = messagebox.askyesno("Konfirmasi Pembayaran", "Apakah Anda ingin melanjutkan pembayaran?")
    if proceed:
        email_address = ps.get_email_by_username(username)
        if not email_address:
            messagebox.showerror("Error", "Alamat email harus diisi.")
            return

        otp = generate_otp()
        struk_beli_peralatan(username, email_address, current_time, total, otp, cart)

        user_otp = simpledialog.askstring("OTP", "Masukkan kode OTP yang telah dikirim ke email Anda:")
        if user_otp == otp:
            save_transaction_data(cart, total, "Non Tunai", current_time, email_address)
            messagebox.showinfo("Sukses", "Pembayaran berhasil, apabila ingin mencetak transaksi silahkan menuju menu printout")
        else:
            messagebox.showerror("Error", "Pembayaran gagal. OTP tidak valid.")

# Halaman Beli Peralatan
def halaman_beli_peralatan():
    global spinbox_vars, username_entry, beli_alat_window
    
    beli_alat_window = Toplevel(window)
    beli_alat_window.geometry("1166x718")
    beli_alat_window.configure(bg='#FFFFFF')

    image_frame = PhotoImage(file=relative_to_assets("pawpaw.png"))
    pawpaw = Label(beli_alat_window, image=image_frame, bg='#FFFFFF')
    pawpaw.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(beli_alat_window, text='HALAMAN BELI PERALATAN', bg='#FFFFFF', foreground='#000000', font='arial 18 bold').place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    
    spinbox_vars = [StringVar(value='0') for _ in range(len(produk_dp))]
    
    for idx, row in produk_dp.iterrows():
        tk.Label(beli_alat_window, text=f"{row['No']}. {row['Nama Peralatan']}", bg='#FFFFFF', foreground='#000000', font='arial 12 bold').place(relx=0.29, rely=0.2 + idx * 0.05, anchor=tk.W)
        tk.Label(beli_alat_window, text=f"Rp. {row['Harga']}", bg='#FFFFFF', foreground='#000000', font='arial 12 bold').place(relx=0.55, rely=0.2 + idx * 0.05, anchor=tk.W)
        Spinbox(beli_alat_window, from_=0, to=100, width=4, font='arial 10', textvariable=spinbox_vars[idx]).place(relx=0.65, rely=0.2 + idx * 0.05, anchor=tk.W)
    
    button_image_total = PhotoImage(file=relative_to_assets("beli.png"))
    tk.Button(beli_alat_window, image=button_image_total, borderwidth=0, highlightthickness=0, command=totalprice, bg='#FFFFFF', activebackground='#FFFFFF').place(relx=0.5, rely=0.13 + len(produk_dp) * 0.05 + 0.1, anchor=tk.CENTER)

    button_image_back = PhotoImage(file=relative_to_assets("button_a.png"))
    tk.Button(
        beli_alat_window,
        image=button_image_back,
        borderwidth=0,
        highlightthickness=0,
        command=back_menu,  # Pastikan fungsi back_menu sudah didefinisikan
        relief="flat",
        bg='#FFFFFF',  # Atur background sama dengan latar belakang window
        activebackground='#FFFFFF'  # Atur background aktif juga
    ).place(
        relx=0.05, rely=0.05, 
        width=100.0, height=44.0
    )
    
    beli_alat_window.mainloop()

def back_menu():
    beli_alat_window.withdraw()
    menu_window.deiconify()
    menu_window.focus_force()

def totalprice():
    global total, cart, current_time, email_user
    total = 0
    cart = []
    order_details = ""

    for idx, row in produk_dp.iterrows():
        qty = int(spinbox_vars[idx].get())
        if qty > 0:
            harga = row['Harga']
            subtotal = qty * harga
            total += subtotal
            cart.append({"Nama Peralatan": row['Nama Peralatan'], "Harga": subtotal})
            order_details += f"{row['Nama Peralatan']}: {qty} x {harga} = {subtotal}\n"

    if total > 0:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ringkasan_pesanan = f"Waktu Pesanan: {current_time}\n"
        for item in cart:
            ringkasan_pesanan += f"- {item['Nama Peralatan']}: Rp{item['Harga']:,}\n"
        ringkasan_pesanan += f"\nTotal Harga: Rp{total:,}"
        ringkasan_order(ringkasan_pesanan)

        email_user = ps.get_email_by_username(username_entry.get())
    else:
        messagebox.showinfo("Order Details", "Tidak ada barang yang dipesan.")

def ringkasan_order(summary_text):
    global detail_window
    detail_window = Toplevel(window)
    detail_window.title("Ringkasan Pesanan")
    detail_window.geometry('750x600')
    detail_window.configure(bg='#FFFFFF')
    
    tk.Label(detail_window, text='Ringkasan Pesanan', bg='#FFFFFF', foreground='#FA57D6', font='arial 18 bold').pack(pady=20)
    tk.Label(detail_window, text=summary_text, bg='#FFFFFF', foreground='#FA57D6', font='arial 12', justify='left', anchor='w').pack(pady=20, padx=20)
    
    tk.Label(detail_window, text='Pilih Metode Pembayaran Anda', bg='#FFFFFF', foreground='#FA57D6', font='arial 12 bold').pack(pady=10)
    
    button_nontunai = tk.Button(detail_window, text='Non Tunai', foreground='#FFFFFF', bg='#FA57D6', width=10, command=confirm_payment)
    button_nontunai.pack(pady=(0, 20)) 

def save_transaction_data(cart, subtotal, method, current_time, user_email):
    with open(r"data/data_transaksi.csv", "a", newline="") as file:
        writer = csv.writer(file)
        transaction_details = [current_time, ", ".join([item["Nama Peralatan"] for item in cart]), subtotal, method, user_email]
        writer.writerow(transaction_details)

# Fungsi Email dan OTP
def struk_beli_makanan(name, email_address, current_time, total, otp, cart):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "petshopkiwkiw@gmail.com"
    smtp_password = "huna bhnh uinc zpgb"

    item_details = "\n".join([f"- {item['Nama Produk']}: Rp{item['Harga']:,}" for item in cart])

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email_address
    msg['Subject'] = "Invoice Pembayaran Pembelian Makanan KiwKiw Petshop"

    body = f"""
==================================================
                RINCIAN PEMBELIAN
==================================================

  Nama                    : {name}
  Waktu pemesanan         : {current_time}
  Total Harga             : Rp {total:,}
  Otp                     : {otp}

  Detail Pembelian:
  {item_details}

==================================================
TERIMA KASIH {name} TELAH BERBELANJA DI KIWKIW PETSHOP
==================================================
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("----Email dengan invoice Pembelian Makanan telah berhasil dikirim ke email anda!----")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

# Fungsi Konfirmasi Pembayaran
def confirm_payment_makanan():
    global email_address, cart, total, current_time
    username = username_entry.get()
    jenis_layanan = "Pembelian Makanan"
    detail_window.destroy()
    proceed = messagebox.askyesno("Konfirmasi Pembayaran", "Apakah Anda ingin melanjutkan pembayaran?")
    if proceed:
        email_address = ps.get_email_by_username(username)
        if not email_address:
            messagebox.showerror("Error", "Alamat email harus diisi.")
            return

        otp = generate_otp()
        struk_beli_makanan(username, email_address, current_time, total, otp, cart)

        user_otp = simpledialog.askstring("OTP", "Masukkan kode OTP yang telah dikirim ke email Anda:")
        if user_otp == otp:
            save_transaction_produk(cart, total, "Non Tunai", current_time, email_address)
            messagebox.showinfo("Sukses", "Pembayaran berhasil, apabila ingin mencetak transaksi silahkan menuju menu printout")
        else:
            messagebox.showerror("Error", "Pembayaran gagal. OTP tidak valid.")

# Halaman Beli Makanan
def halaman_beli_makan():
    global spinbox_vars, username_entry, beli_makan_window
    
    beli_makan_window = Toplevel(window)
    beli_makan_window.geometry("1166x718")
    beli_makan_window.configure(bg='#FFFFFF')

    image_frame = PhotoImage(file=relative_to_assets("pawpaw.png"))
    pawpaw = Label(beli_makan_window, image=image_frame, bg='#FFFFFF')
    pawpaw.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(beli_makan_window, text='KASIR TOKO PETSHOP', bg='#FFFFFF', foreground='#000000', font='arial 18 bold').place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    
    spinbox_vars = [StringVar(value='0') for _ in range(len(produk_df))]
    
    for idx, row in produk_df.iterrows():
        tk.Label(beli_makan_window, text=f"{row['No']}. {row['Nama Produk']}", bg='#FFFFFF', foreground='#000000', font='arial 12 bold').place(relx=0.29, rely=0.2 + idx * 0.05, anchor=tk.W)
        tk.Label(beli_makan_window, text=f"Rp. {row['Harga']}", bg='#FFFFFF', foreground='#000000', font='arial 12 bold').place(relx=0.55, rely=0.2 + idx * 0.05, anchor=tk.W)
        Spinbox(beli_makan_window, from_=0, to=100, width=4, font='arial 10', textvariable=spinbox_vars[idx]).place(relx=0.65, rely=0.2 + idx * 0.05, anchor=tk.W)
    
    button_image_total = PhotoImage(file=relative_to_assets("beli.png"))
    tk.Button(beli_makan_window, image=button_image_total, borderwidth=0, highlightthickness=0, command=totalbeli, bg='#FFFFFF', activebackground='#FFFFFF').place(relx=0.5, rely=0.13 + len(produk_df) * 0.05 + 0.1, anchor=tk.CENTER)

    button_image_kembali = PhotoImage(file=relative_to_assets("button_a.png"))
    tk.Button(
        beli_makan_window,
        image=button_image_kembali,
        borderwidth=0,
        highlightthickness=0,
        command=kembali_menu,  # Pastikan fungsi kembali_menu sudah didefinisikan
        relief="flat",
        bg='#FFFFFF',  # Atur background sama dengan latar belakang window
        activebackground='#FFFFFF'  # Atur background aktif juga
    ).place(
        relx=0.05, rely=0.05, 
        width=100.0, height=44.0
    )

    beli_makan_window.mainloop()


def kembali_menu():
    beli_makan_window.withdraw()
    menu_window.deiconify()
    menu_window.focus_force()

def totalbeli():
    global total, cart, current_time, email_user
    total = 0
    cart = []
    order_details = ""

    for idx, row in produk_df.iterrows():
        qty = int(spinbox_vars[idx].get())
        if qty > 0:
            harga = row['Harga']
            subtotal = qty * harga
            total += subtotal
            cart.append({"Nama Produk": row['Nama Produk'], "Harga": subtotal})
            order_details += f"{row['Nama Produk']}: {qty} x {harga} = {subtotal}\n"

    if total > 0:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ringkasan_pesanan = f"Waktu Pesanan: {current_time}\n"
        for item in cart:
            ringkasan_pesanan += f"- {item['Nama Produk']}: Rp{item['Harga']:,}\n"
        ringkasan_pesanan += f"\nTotal Harga: Rp{total:,}"
        show_order_summary(ringkasan_pesanan)

        email_user = ps.get_email_by_username(username_entry.get())
    else:
        messagebox.showinfo("Order Details", "Tidak ada barang yang dipesan.")

def show_order_summary(summary_text):
    global detail_window
    detail_window = Toplevel(window)
    detail_window.title("Ringkasan Pesanan")
    detail_window.geometry('750x600')
    detail_window.configure(bg='#FFFFFF')
    
    tk.Label(detail_window, text='Ringkasan Pesanan', bg='#FFFFFF', foreground='#FA57D6', font='arial 18 bold').pack(pady=20)
    tk.Label(detail_window, text=summary_text, bg='#FFFFFF', foreground='#FA57D6', font='arial 12', justify='left', anchor='w').pack(pady=20, padx=20)
    
    tk.Label(detail_window, text='Pilih Metode Pembayaran Anda', bg='#FFFFFF', foreground='#FA57D6', font='arial 12 bold').pack(pady=10)
    
    button_nontunai = tk.Button(detail_window, text='Non Tunai', foreground='#FFFFFF', bg='#FA57D6', width=10, command=confirm_payment_makanan)
    button_nontunai.pack(pady=(0, 20)) 

def save_transaction_produk(cart, subtotal, method, current_time, user_email):
    with open(r"data/data_transaksi.csv", "a", newline="") as file:
        writer = csv.writer(file)
        transaction_details = [current_time, ", ".join([item["Nama Produk"] for item in cart]), subtotal, method, user_email]
        writer.writerow(transaction_details)

def halaman_layanan():
    global window, layanan_window
    layanan_window = Toplevel(window)
    layanan_window.geometry("1166x718")
    layanan_window.configure(bg="#BDCBFC")
    
    canvas = Canvas(
        layanan_window,
        bg = "#BDCBFC",
        height = 718,
        width = 1166,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    # Store the images in the window object to keep them in memory
    layanan_window.image_image_1 = PhotoImage(file=relative_to_assets("image_t.png"))
    image_1 = canvas.create_image(583.0, 359.0, image=layanan_window.image_image_1)

    layanan_window.image_image_2 = PhotoImage(file=relative_to_assets("image_u.png"))
    image_2 = canvas.create_image(598.0, 192.0, image=layanan_window.image_image_2)

    layanan_window.image_image_3 = PhotoImage(file=relative_to_assets("image_i.png"))
    image_3 = canvas.create_image(819.0, 363.0, image=layanan_window.image_image_3)

    layanan_window.image_image_4 = PhotoImage(file=relative_to_assets("image_r.png"))
    image_4 = canvas.create_image(410.0, 378.0, image=layanan_window.image_image_4)

    layanan_window.button_image_t = PhotoImage(file=relative_to_assets("button_t.png"))
    button_t = Button(
        layanan_window,
        image=layanan_window.button_image_t,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_konsultasi,relief="flat")
    button_t.place(
        x=316.0,
        y=504.0,
        width=188.0,
        height=46.0
    )

    layanan_window.button_image_u = PhotoImage(file=relative_to_assets("button_u.png"))
    button_u = Button(
        layanan_window,
        image=layanan_window.button_image_u,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_grooming, relief="flat"
    )
    button_u.place(
        x=740.0,
        y=510.0,
        width=188.0,
        height=46.0
    )
        
    button_image_balik = PhotoImage(file=relative_to_assets("button_a.png"))
    tk.Button(
        layanan_window,
        image=button_image_balik,
        borderwidth=0,
        highlightthickness=0,
        command=kembali_lagi,  # Pastikan fungsi back_menu sudah didefinisikan
        relief="flat",
        bg='#FFFFFF',  # Atur background sama dengan latar belakang window
        activebackground='#FFFFFF'  # Atur background aktif juga
    ).place(
        relx=0.05, rely=0.05, 
        width=100.0, height=44.0
    )
    window.resizable(False, False)
    window.mainloop()

def kembali_lagi():
    layanan_window.withdraw()
    menu_window.deiconify()
    menu_window.focus_force()

genai.configure(api_key="AIzaSyBghRPbz_M_CWi7hObukO3jxZEPACH4HMo")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro", safety_settings=safety_settings, generation_config=generation_config)

chat_session = model.start_chat(history=[])

def send_message(event=None):
    user_input = input_entry.get("1.0", tk.END).strip()
    input_entry.delete("1.0", tk.END)

    if user_input:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, "You: " + user_input + "\n")
        chat_history.config(state=tk.DISABLED)

        response = chat_session.send_message(user_input)
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, "Dokter: " + response.text + "\n")
        chat_history.config(state=tk.DISABLED)

def halaman_konsultasi():
    global input_entry, chat_history

    konsultasi_window = Toplevel(window)
    konsultasi_window.geometry("600x400")
    konsultasi_window.configure(bg="#BDCBFC")
    konsultasi_window.title("Konsultasi")

    # Text area for displaying chat history
    chat_history = scrolledtext.ScrolledText(konsultasi_window, width=50, height=20, state=tk.DISABLED)
    chat_history.pack(padx=10, pady=10)

    # Entry field for user input
    input_entry = tk.Text(konsultasi_window, width=50, height=3)
    input_entry.bind("<Return>", send_message)
    input_entry.pack(padx=10, pady=10)

    # Send button
    send_button = tk.Button(konsultasi_window, text="Send", command=send_message)
    send_button.pack(padx=10, pady=5)

    # Focus on input field when the window is opened
    input_entry.focus()

def send_email(recipient, subject, body):
    # Konfigurasi pengiriman email
    sender_email = "petshopkiwkiw.com"
    sender_password = "huna bhnh uinc zpgb"

    # Membuat pesan email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        # Mengirim email
        server = smtplib.SMTP_SSL('smtp.example.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def generate_otp():
    """Generate One Time Password (OTP)."""
    otp = ''.join(random.choices(string.ascii_letters, k=5))
    return otp

def struk_konsultasi_grooming(name, email_address, current_time, date, waktu_awal, otp):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = username_entry.get()
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "petshopkiwkiw@gmail.com"
    smtp_password = "huna bhnh uinc zpgb"

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email_address
    msg['Subject'] = "Invoice Pembayaran Konsultasi KiwKiw Petshop"

    body = f"""
==================================================
                JAM GROOMING
==================================================

  Nama                    : {name}
  Waktu pemesanan         : {current_time}  
  Jam Konsul              : {waktu_awal}
  Tanggal                 : {date}
  Harga                   : Rp 100.000,00
  Otp                     : {otp}

  MOHON DITUNGGU KEHADIRAN DARI KAMI !

==================================================
TERIMA KASIH {name} TELAH GROOMING DI KIWKIW PETSHOP
==================================================
    """
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("----Email dengan invoice Jadwal Grooming telah berhasil dikirim ke email anda!----")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

def halaman_grooming():
    global current_time, name
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = username_entry.get()
    
    def submit():
        date = cal.get_date()  # This returns a datetime.date object
        start_hour = start_hour_spinbox.get()
        start_minute = start_minute_spinbox.get()
        end_hour = end_hour_spinbox.get()
        end_minute = end_minute_spinbox.get()
        
        start_time = f"{start_hour}:{start_minute}"
        end_time = f"{end_hour}:{end_minute}"

        # Convert to datetime objects for comparison
        now = datetime.datetime.now()
        selected_start_time = datetime.datetime.strptime(start_time, '%H:%M').time()
        selected_end_time = datetime.datetime.strptime(end_time, '%H:%M').time()

        selected_start_datetime = datetime.datetime.combine(date, selected_start_time)
        selected_end_datetime = datetime.datetime.combine(date, selected_end_time)
        
        waktu_awal = selected_start_datetime.time()
        waktu_akhir = selected_end_datetime.time()
        
        waktu_buka = datetime.time(8, 0)
        waktu_tutup = datetime.time(15, 0)

        if selected_start_datetime < now:
            messagebox.showerror("Error", "Waktu yang dipilih sudah berlalu. Silakan pilih waktu yang valid.")
            return

        if waktu_awal >= waktu_akhir:
            messagebox.showerror("Error", "Waktu mulai harus sebelum waktu selesai. Silakan coba lagi.")
            return

        if not (waktu_buka <= waktu_awal < waktu_tutup):
            messagebox.showerror("Error", "Grooming hanya tersedia dari jam 8 pagi sampai 3 sore. Silakan pilih waktu di antara waktu tersebut.")
            return

        if not (waktu_buka <= waktu_akhir < waktu_tutup):
            messagebox.showerror("Error", "Grooming hanya tersedia dari jam 8 pagi sampai 3 sore. Silakan pilih waktu di antara waktu tersebut.")
            return

        # Menampilkan window kecil dengan detail transaksi
        detail_window = tk.Toplevel(root)
        detail_window.title("Detail Transaksi")
        detail_window.geometry("300x200")
        
        detail_label = ttk.Label(detail_window, text=f"Tanggal: {date}\nWaktu: {start_time} - {end_time}\nHarga: Rp 100,000")
        detail_label.pack(pady=20)

        def confirm_payment():
            global email_address
            username = username_entry.get()
            jenis_layanan = "Grooming"
            detail_window.destroy()
            proceed = messagebox.askyesno("Konfirmasi Pembayaran", "Apakah Anda ingin melanjutkan pembayaran?")
            if proceed:
                # Mendapatkan email pengguna menggunakan fungsi ps.get_email_by_username
                email_address = ps.get_email_by_username(username)
                if not email_address:
                    messagebox.showerror("Error", "Alamat email harus diisi.")
                    return
                
                otp = generate_otp()
                struk_konsultasi_grooming(name, email_address, current_time, date, waktu_awal, otp)

                # Meminta input OTP dari pengguna
                user_otp = simpledialog.askstring("OTP", "Masukkan kode OTP yang telah dikirim ke email Anda:")
                if user_otp == otp:
                    # Simpan data transaksi ke CSV
                    save_transaction_layanan(jenis_layanan, current_time, email_address, date, waktu_awal)
                    messagebox.showinfo("Sukses", "Pembayaran berhasil, apabila ingin mencetak transaksi silahkan menuju menu printout")
                else:
                    messagebox.showerror("Error", "Pembayaran gagal. OTP tidak valid.")

        confirm_button = ttk.Button(detail_window, text="Lanjutkan Pembayaran", command=confirm_payment)
        confirm_button.pack(pady=20)

    root = tk.Tk()
    root.title("Grooming Schedule")
    root.geometry("600x400")  # Ukuran window diubah menjadi lebih kecil
    root.configure(bg="#FFC0CB")  # Latar belakang warna pink

    # Calendar
    cal_label = ttk.Label(root, text="Select Date:", background="#FFC0CB")
    cal_label.pack(pady=10)
    cal = DateEntry(root, width=12, background='#ADD8E6', foreground='white', borderwidth=2)
    cal.pack(pady=10)

    # Start time
    start_time_frame = ttk.Frame(root)
    start_time_frame.pack(pady=10)

    start_time_label = ttk.Label(start_time_frame, text="Start Time:", background="#FFC0CB")
    start_time_label.pack(side=tk.LEFT, padx=5)

    start_hour_spinbox = ttk.Spinbox(start_time_frame, from_=0, to=23, width=3, format="%02.0f", foreground="#0000FF")
    start_hour_spinbox.pack(side=tk.LEFT)
    start_hour_spinbox.set("08")

    start_minute_spinbox = ttk.Spinbox(start_time_frame, from_=0, to=59, width=3, format="%02.0f", foreground="#0000FF")
    start_minute_spinbox.pack(side=tk.LEFT)
    start_minute_spinbox.set("00")

    # End time
    end_time_frame = ttk.Frame(root)
    end_time_frame.pack(pady=10)

    end_time_label = ttk.Label(end_time_frame, text="End Time:", background="#FFC0CB")
    end_time_label.pack(side=tk.LEFT, padx=5)

    end_hour_spinbox = ttk.Spinbox(end_time_frame, from_=0, to=23, width=3, format="%02.0f", foreground="#0000FF")
    end_hour_spinbox.pack(side=tk.LEFT)
    end_hour_spinbox.set("09")

    end_minute_spinbox = ttk.Spinbox(end_time_frame, from_=0, to=59, width=3, format="%02.0f", foreground="#0000FF")
    end_minute_spinbox.pack(side=tk.LEFT)
    end_minute_spinbox.set("00")

    # Submit button
    submit_btn = ttk.Button(root, text="Pilih waktu", command=submit)
    submit_btn.pack(pady=20)

    root.mainloop()

def save_transaction_layanan (jenis_layanan, current_time, email_address, date, waktu_awal):
    jenis_layanan = "Grooming"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/data_riwayat_grooming.csv", "a", newline="") as file:
        writer = csv.writer(file)
        transaction_details = [current_time, jenis_layanan, date, waktu_awal, email_address]
        writer.writerow(transaction_details)

# Run the application

def back_login():
    reg_window.withdraw()
    window.deiconify()
    window.focus_force()

def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Praktikum Prokom\Tubes\ProjectPetshop\ProjectPetshop\image")
    return ASSETS_PATH / Path(path)

halaman_login()