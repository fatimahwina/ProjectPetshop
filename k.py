import email
from tkinter import *
from tkinter import messagebox, Toplevel
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
import os
import platform
import openai
from fpdf import FPDF
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

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
    with open('C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = row
            print("Checking:", a, b)
            if username == a and password == b:
                sukses = True
                break
    if sukses == True:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.withdraw()  # Hide the login window
        email_user = ps.get_email_by_username(username)
        halaman_menu()
    else:
        print("=" * 50)
        print("Username atau Password yang anda masukkan salah")
        print("=" * 50)
        login()

    if sukses:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.withdraw()  # Hide the login window
        halaman_menu()  # Open the menu window
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def signup():
    name = username.get()
    password = user_password.get()
    email = user_email.get()

    print(f"Username: {name}, Password: {password}, Email: {email}")  # Debugging

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
                    with open('C:/Praktikum prokom/ProjectPetshop/data/login.csv', 'a', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([name, password, email])
                    messagebox.showinfo(title="Success", message="Register berhasil, silahkan login")
                    otp_window.destroy()
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
        relief="ridge"
    )
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
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        741.0, 193.0,
        anchor="nw",
        text="Sign in",
        fill="#FF27A8",
        font=("kavoon regular", 40 * -1)
    )

    canvas.create_text(
        696.0, 348.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    window.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(298.0, 343.0, image=window.image_image_3)

    canvas.create_text(
        817.0, 487.0,
        anchor="nw",
        text="or",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    window.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(838.0, 321.0, image=window.entry_image_1)

    username_entry = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username_entry.place(
        x=707.0, y=299.0,
        width=262.0, height=42.0
    )

    window.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(838.0, 399.0, image=window.entry_image_2)

    password_entry = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    password_entry.place(
        x=707.0, y=377.0,
        width=262.0, height=42.0
    )

    window.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    Button(
        image=window.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_register,
        relief="flat"
    ).place(x=691.0, y=508.0, width=294.0, height=44.0)

    window.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    Button(
        image=window.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat"
    ).place(
        x=691.0, y=443.0,
        width=294.0, height=44.0
    )

    window.resizable(False, False)
    window.mainloop()

def halaman_register():
    global username, user_password, user_email, reg_window

    reg_window = Toplevel(window)
    reg_window.geometry("1166x718")
    reg_window.configure(bg="#ACCDFF")

    canvas = Canvas(
        reg_window,
        bg="#ACCDFF",
        height=718,
        width=1166,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    
    reg_window.image_image_1 = PhotoImage(file=relative_to_assets("image_a.png"))
    canvas.create_image(583.0, 359.0, image=reg_window.image_image_1)

    reg_window.image_image_2 = PhotoImage(file=relative_to_assets("image_b.png"))
    canvas.create_image(837.0, 368.0, image=reg_window.image_image_2)

    reg_window.entry_image_1 = PhotoImage(file=relative_to_assets("entry_a.png"))
    canvas.create_image(838.0, 465.0, image=reg_window.entry_image_1)
    user_email = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    user_email.place(
        x=707.0, y=443.0,
        width=262.0, height=42.0
    )

    canvas.create_text(
        696.0, 257.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        741.0, 193.0,
        anchor="nw",
        text="Register",
        fill="#FF27A8",
        font=("Kavoon Regular", 40 * -1)
    )

    reg_window.button_image_1 = PhotoImage(file=relative_to_assets("button_a.png"))
    Button(
        reg_window,
        image=reg_window.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back_login,
        relief="flat").place(x=691.0, y=508.0, width=294.0, height=44.0)

    canvas.create_text(
        696.0, 348.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        696.0, 414.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    reg_window.image_image_3 = PhotoImage(file=relative_to_assets("image_c.png"))
    canvas.create_image(298.0, 343.0, image=reg_window.image_image_3)

    reg_window.entry_image_2 = PhotoImage(file=relative_to_assets("entry_b.png"))
    canvas.create_image(838.0, 308.0, image=reg_window.entry_image_2)
    username = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username.place(
        x=707.0, y=286.0,
        width=262.0, height=42.0
    )

    reg_window.entry_image_3 = PhotoImage(file=relative_to_assets("entry_c.png"))
    canvas.create_image(838.0, 387.0, image=reg_window.entry_image_3)
    user_password = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    user_password.place(
        x=707.0, y=365.0,
        width=262.0, height=42.0
    )
    
    reg_window.button_image_2 = PhotoImage(file=relative_to_assets("button_b.png"))
    Button(
        reg_window, image=reg_window.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=signup,
        relief="flat"
    ).place(
        x=691.0, y=508.0,
        width=294.0, height=44.0
    )

    reg_window.resizable(False, False)
    reg_window.mainloop()

def halaman_menu():
    global window

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
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        169.0,
        1146.0,
        1283.0,
        fill="#FFFFFF",
        outline=""
    )

    image_pawpaw = PhotoImage(
        file=relative_to_assets("pawpaw.png"))
    pawpaw = canvas.create_image(
        583.0,
        100.0,
        image=image_pawpaw
    )

    image_image_v = PhotoImage(file=relative_to_assets("image_v.png"))
    image_1 = canvas.create_image(807.0, 523.0, image=image_image_v)

    image_image_w = PhotoImage(file=relative_to_assets("image_w.png"))
    image_w = canvas.create_image(575.0, 272.0, image=image_image_w)

    image_image_x = PhotoImage(file=relative_to_assets("image_x.png"))
    image_x = canvas.create_image(250.0, 272.0, image=image_image_x)

    image_image_y = PhotoImage(file=relative_to_assets("image_y.png"))
    image_y = canvas.create_image(574.0, 102.0, image=image_image_y)

    canvas.create_text(
        450.0,
        80.0,
        anchor="nw",
        text="Pilihan Menu",
        fill="#FFFFFF",
        font=("Candy Beans", 48 * -1)
    )

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
        command=lambda: print("button_v clicked"),
        relief="flat"
    )
    button_v.image = button_image_v  # Keep a reference to the image
    button_v.place(
        x=469.0,
        y=362.0,
        width=207.0,
        height=40.0
    )

    button_image_w = PhotoImage(file=relative_to_assets("button_w.png"))
    button_w = Button(
        menu_window,
        image=button_image_w,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_w clicked"),
        relief="flat"
    )
    button_w.image = button_image_w  # Keep a reference to the image
    button_w.place(
        x=800.0,
        y=362.0,
        width=207.0,
        height=40.0
    )

    button_image_x = PhotoImage(file=relative_to_assets("button_x.png"))
    button_x = Button(
        menu_window,
        image=button_image_x,
        borderwidth=0,
        highlightthickness=0,
        command=printout,
        relief="flat"
    )
    button_x.image = button_image_x  # Keep a reference to the image
    button_x.place(
        x=302.0,
        y=619.0,
        width=207.0,
        height=40.0
    )

    button_image_y = PhotoImage(file=relative_to_assets("button_y.png"))
    button_y = Button(
        menu_window,
        image=button_image_y,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_y clicked"),
        relief="flat"
    )
    button_y.image = button_image_y  # Keep a reference to the image
    button_y.place(
        x=708.0,
        y=619.0,
        width=207.0,
        height=40.0
    )

    button_image_z = PhotoImage(file=relative_to_assets("button_z.png"))
    button_z = Button(
        menu_window,
        image=button_image_z,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_beli_makan,
        relief="flat"
    )
    button_z.image = button_image_z  # Keep a reference to the image
    button_z.place(
        x=125.0,
        y=362.0,
        width=246.0,
        height=35.0
    )

    menu_window.resizable(False, False)
    menu_window.mainloop()

produk_df = pd.read_csv('data/Daftar_Produk.csv')


def halaman_beli_makan():
    global spinbox_vars
    
    beli_makan_window = Toplevel(window)
    beli_makan_window.geometry("1166x718")
    beli_makan_window.configure(bg='#FFFFFF')

    image_frame = PhotoImage(file=relative_to_assets("frame.png"))
    pawpaw = Label(beli_makan_window, image=image_frame)
    pawpaw.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tk.Label(beli_makan_window, text='KASIR TOKO PETSHOP', bg='#31c6d4', foreground='#fef5ac', font='arial 18 bold').place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    
    button_image_total = PhotoImage(file=relative_to_assets("beli.png"))
    tk.Button(beli_makan_window, image=button_image_total, borderwidth=0, highlightthickness=0, command=totalbeli).place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    spinbox_vars = [StringVar(value='0') for _ in range(len(produk_df))]
    
    for idx, row in produk_df.iterrows():
        tk.Label(beli_makan_window, text=f"{row['No']}. {row['Nama Produk']}", bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(relx=0.2, rely=0.1 + idx * 0.05, anchor=tk.W)
        tk.Label(beli_makan_window, text=f"Rp. {row['Harga']}", bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(relx=0.6, rely=0.1 + idx * 0.05, anchor=tk.W)
        Spinbox(beli_makan_window, from_=0, to=100, width=4, font='arial 10', textvariable=spinbox_vars[idx]).place(relx=0.7, rely=0.1 + idx * 0.05, anchor=tk.W)

    beli_makan_window.mainloop()

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

        email_user = ps.get_email_by_username()
    else:
        messagebox.showinfo("Order Details", "Tidak ada barang yang dipesan.")

def show_order_summary(summary_text):
    summary_window = Toplevel(window)
    summary_window.title("Ringkasan Pesanan")
    summary_window.geometry('750x600')
    summary_window.configure(bg='#FFFFFF')
    
    tk.Label(summary_window, text='Ringkasan Pesanan', bg='#FFFFFF', foreground='#FA57D6', font='arial 18 bold').pack(pady=20)
    tk.Label(summary_window, text=summary_text, bg='#FFFFFF', foreground='#FA57D6', font='arial 12', justify='left', anchor='w').pack(pady=20, padx=20)
    
    tk.Label(summary_window, text='Pilih Metode Pembayaran Anda', bg='#FFFFFF', foreground='#FA57D6', font='arial 12 bold').pack(pady=10)
    
    button_nontunai = tk.Button(summary_window, text='Non Tunai', foreground='#FFFFFF', bg='#FA57D6', width=10, command=lambda: payment_method("Non Tunai"))
    button_nontunai.pack(pady=(0, 20)) 

def payment_method(method):
    save_transaction_data(cart, total, method, current_time, email_user)
    messagebox.showinfo("Metode Pembayaran", f"Anda memilih metode pembayaran: {method}")

def save_transaction_data(cart, subtotal, method, current_time, user_email):
    with open(r"C:\Praktikum prokom\ProjectPetshop\data\data_transaksi.csv", "a", newline="") as file:
        writer = csv.writer(file)
        transaction_details = [current_time, ", ".join([item["Nama Produk"] for item in cart]), subtotal, method, user_email]
        writer.writerow(transaction_details)

def printout():
    email_user = get_email_by_username(username_entry)  # Pastikan Anda memiliki cara untuk mendapatkan email pengguna
    pdf_filename = generate_transaction_pdf(email_user)
    if pdf_filename:
        send_email_with_pdf(email_user, pdf_filename)

def generate_transaction_pdf(email_user):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.cell(200, 10, txt="Laporan Transaksi KiwKiw Petshop", ln=True, align='C')
    pdf.ln(10)

    # Table Header
    pdf.cell(40, 10, txt="Tanggal", border=1)
    pdf.cell(80, 10, txt="Produk", border=1)
    pdf.cell(30, 10, txt="Total Harga", border=1)
    pdf.cell(40, 10, txt="Metode Pembayaran", border=1)
    pdf.ln()

    # Read transaction data
    transactions = []
    with open(r'C:\Praktikum prokom\ProjectPetshop\data\data_transaksi.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            date, products, total, payment_method, email = row
            if email == email_user:
                transactions.append(row)

    if not transactions:
        print("Tidak ada transaksi untuk email ini.")
        return None

    # Add transactions to PDF
    for transaction in transactions:
        pdf.cell(40, 10, txt=transaction[0], border=1)
        pdf.cell(80, 10, txt=transaction[1], border=1)
        pdf.cell(30, 10, txt=transaction[2], border=1)
        pdf.cell(40, 10, txt=transaction[3], border=1)
        pdf.ln()

    # Save PDF
    pdf_filename = f"transaksi_{email_user}.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

def send_email_with_pdf(email_user, pdf_filename):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "petshopkiwkiw@gmail.com"
    smtp_password = "huna bhnh uinc zpgb"

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email_user
    msg['Subject'] = "Laporan Transaksi KiwKiw Petshop"

    body = "Terlampir adalah laporan transaksi Anda."
    msg.attach(MIMEText(body, 'plain'))

    # Attach PDF
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {pdf_filename}",
    )
    msg.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Sukses", "Email dengan laporan transaksi telah berhasil dikirim ke email Anda!")
    except Exception as e:
        messagebox.showerror("Gagal", f"Gagal mengirim email: {e}")

def back_login():
    reg_window.withdraw()
    window.deiconify()
    window.focus_force()

def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Praktikum prokom\\ProjectPetshop\\image")
    return ASSETS_PATH / Path(path)

def get_email_by_username(username_entry):
    with open('C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username_entry:
                return row[2]  # Mengembalikan email dari baris yang sesuai dengan username
    return None  # Jika username tidak ditemukan


halaman_login()