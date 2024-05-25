from tkinter import *
from tkinter import messagebox, Toplevel
import csv
from pathlib import Path
import tkinter as tk
import pandas as pd
import datetime
import smtplib
from fpdf import FPDF
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
    with open('C:/Praktikum prokom/ProjectPetshop/data/login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = row
            print("Checking:", a, b)
            if username == a and password == b:
                sukses = True
                email_user = c
                break
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
            kode_otp = generate_otp()
            print(f"OTP generated: {kode_otp}")  # Debugging
            send_otp_email(email, kode_otp)
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
        text="Sign up",
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

    canvas.create_text(
        696.0, 421.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    reg_window.entry_image_2 = PhotoImage(file=relative_to_assets("entry_b.png"))
    canvas.create_image(838.0, 376.0, image=reg_window.entry_image_2)
    user_password = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    user_password.place(
        x=707.0, y=354.0,
        width=262.0, height=42.0
    )

    reg_window.entry_image_3 = PhotoImage(file=relative_to_assets("entry_c.png"))
    canvas.create_image(838.0, 287.0, image=reg_window.entry_image_3)
    username = Entry(
        reg_window,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username.place(
        x=707.0, y=265.0,
        width=262.0, height=42.0
    )

    reg_window.button_image_1 = PhotoImage(file=relative_to_assets("button_a.png"))
    Button(
        reg_window,
        image=reg_window.button_image_1,
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
    global window1

    window1 = Toplevel()
    window1.geometry("1166x718")
    window1.configure(bg="white")

    canvas = Canvas(
        window1,
        bg="white",
        height=718,
        width=1166,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    window1.image_image_1 = PhotoImage(file=relative_to_assets("image_c.png"))
    canvas.create_image(583.0, 359.0, image=window1.image_image_1)

    canvas.create_text(
        200.0, 0.0,
        anchor="nw",
        text="Selamat Datang",
        fill="#000000",
        font=("Inter", 50 * -1)
    )

    window1.image_image_2 = PhotoImage(file=relative_to_assets("image_d.png"))
    canvas.create_image(582.0, 356.0, image=window1.image_image_2)

    window1.button_image_1 = PhotoImage(file=relative_to_assets("button_b.png"))
    button_b = Button(
        window1,
        image=window1.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_stock,
        relief="flat"
    )
    button_b.place(x=300.0, y=257.0, width=273.0, height=102.0)

    window1.button_image_2 = PhotoImage(file=relative_to_assets("button_c.png"))
    button_c = Button(
        window1,
        image=window1.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_beli,
        relief="flat"
    )
    button_c.place(x=600.0, y=257.0, width=273.0, height=102.0)

    window1.resizable(False, False)
    window1.mainloop()

def halaman_stock():
    def show_data():
        df = pd.read_csv("C:/Praktikum prokom/ProjectPetshop/data/stockbarang.csv")
        print("Stock DataFrame:\n", df)  # Debugging
        textbox.delete(1.0, END)
        textbox.insert(END, df.to_string(index=False))

    stock_window = Toplevel(window1)
    stock_window.geometry("1166x718")
    stock_window.configure(bg="white")

    canvas = Canvas(
        stock_window,
        bg="white",
        height=718,
        width=1166,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    stock_window.image_image_1 = PhotoImage(file=relative_to_assets("image_c.png"))
    canvas.create_image(583.0, 359.0, image=stock_window.image_image_1)

    stock_window.image_image_2 = PhotoImage(file=relative_to_assets("image_d.png"))
    canvas.create_image(582.0, 356.0, image=stock_window.image_image_2)

    textbox = Text(stock_window, height=20, width=50)
    textbox.pack(pady=20)

    window1.button_image_1 = PhotoImage(file=relative_to_assets("button_b.png"))
    show_button = Button(
        stock_window,
        text="Show Data",
        command=show_data
    )
    show_button.pack(pady=10)

def halaman_beli():
    global entry_jumlah, entry_barang

    beli_window = Toplevel(window1)
    beli_window.geometry("1166x718")
    beli_window.configure(bg="white")

    canvas = Canvas(
        beli_window,
        bg="white",
        height=718,
        width=1166,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    beli_window.image_image_1 = PhotoImage(file=relative_to_assets("image_c.png"))
    canvas.create_image(583.0, 359.0, image=beli_window.image_image_1)

    beli_window.image_image_2 = PhotoImage(file=relative_to_assets("image_d.png"))
    canvas.create_image(582.0, 356.0, image=beli_window.image_image_2)

    canvas.create_text(
        320.0, 257.0,
        anchor="nw",
        text="Barang yang dibeli:",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_barang = Entry(beli_window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_barang.place(x=320.0, y=287.0, width=200.0, height=25.0)

    canvas.create_text(
        320.0, 317.0,
        anchor="nw",
        text="Jumlah:",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_jumlah = Entry(beli_window, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_jumlah.place(x=320.0, y=347.0, width=200.0, height=25.0)

    beli_window.button_image_1 = PhotoImage(file=relative_to_assets("button_b.png"))
    Button(
        beli_window,
        image=beli_window.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=totalbeli,
        relief="flat"
    ).place(x=540.0, y=257.0, width=273.0, height=102.0)

    beli_window.resizable(False, False)
    beli_window.mainloop()

def totalbeli():
    jumlah = int(entry_jumlah.get())
    barang = entry_barang.get()
    total_harga = 0
    df = pd.read_csv("C:/Praktikum prokom/ProjectPetshop/data/stockbarang.csv")
    stock_dict = df.set_index('Barang')['Stock'].to_dict()
    price_dict = df.set_index('Barang')['Harga'].to_dict()

    if barang in stock_dict:
        if jumlah <= stock_dict[barang]:
            total_harga = jumlah * price_dict[barang]
            stock_dict[barang] -= jumlah
            df.loc[df['Barang'] == barang, 'Stock'] = stock_dict[barang]
            df.to_csv("C:/Praktikum prokom/ProjectPetshop/data/stockbarang.csv", index=False)
            save_transaction(barang, jumlah, total_harga)
            generate_transaction_pdf(barang, jumlah, total_harga)
            send_email_with_pdf(email_user)
            messagebox.showinfo(title="Success", message=f"Total Harga: {total_harga}")
        else:
            messagebox.showerror(title="Error", message="Jumlah barang tidak mencukupi")
    else:
        messagebox.showerror(title="Error", message="Barang tidak ditemukan")

def save_transaction(barang, jumlah, total_harga):
    file_path = 'C:/Praktikum prokom/ProjectPetshop/data/data_transaksi.csv'
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([barang, jumlah, total_harga, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

def generate_transaction_pdf(barang, jumlah, total_harga):
    c = canvas.Canvas('C:/Praktikum prokom/ProjectPetshop/data/transaction.pdf', pagesize=letter)
    c.drawString(100, 750, f"Barang: {barang}")
    c.drawString(100, 735, f"Jumlah: {jumlah}")
    c.drawString(100, 720, f"Total Harga: {total_harga}")
    c.save()

def send_email_with_pdf(receiver_email):
    sender_email = "projectpetshop2023@gmail.com"
    password = "project12345"
    subject = "Transaction Receipt"
    body = "Please find the attached PDF for your transaction receipt."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    filename = 'C:/Praktikum prokom/ProjectPetshop/data/transaction.pdf'
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

halaman_login()
