import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import pandas as pd
import smtplib
import ssl
import re
from fpdf import FPDF
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from tkinter import messagebox, Toplevel

def read(nama_file):
    data = pd.read_csv(nama_file)
    df = pd.DataFrame(data)
    return df

def generate_otp():
    otp = ''.join(random.choices('0123456789', k=6))  # Menghasilkan OTP acak 6 digit
    return otp

def send_otp_email(email_user, otp):
    # Konfigurasi SMTP Server
    smtp_server = "smtp.gmail.com"  # Ganti dengan SMTP server Anda
    smtp_port = 587  # Ganti dengan port SMTP yang sesuai
    smtp_username = "petshopkiwkiw@gmail.com"  # Ganti dengan username SMTP Anda
    smtp_password = "huna bhnh uinc zpgb"  # Ganti dengan password SMTP Anda

    # Membangun Pesan Email
    msg = MIMEMultipart()
    msg['From'] = "petshopkiwkiw@gmail.com"  # Ganti dengan alamat email Anda
    msg['To'] = email_user
    msg['Subject'] = "KIW KIW PETSHOP"

    # Isi Pesan Email
    body = f"Berikut adalah kode OTP Anda untuk registrasi aplikasi: {otp}"
    msg.attach(MIMEText(body, 'plain'))

    # Mengirim Email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Email OTP berhasil dikirim!")
    except Exception as e:
        print(f"Error: {e}")

def get_email_by_username(username):
    with open('C:\\Praktikum prokom\\ProjectPetshop\\data\\login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return row[2]  # Mengembalikan email dari baris yang sesuai dengan username
    return None  # Jika username tidak ditemukan

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
    with open(r'data\data_transaksi.csv', 'r') as file:
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

def struk_konsultasi(name, email,tanggal,waktu_awal, waktu_akhir):
    smtp_server = "smtp.gmail.com"  # Ganti dengan SMTP server Anda
    smtp_port = 587  # Ganti dengan port SMTP yang sesuai
    smtp_username = "petshopkiwkiw@gmail.com"  # Ganti dengan username SMTP Anda
    smtp_password = "huna bhnh uinc zpgb"  # Ganti dengan password SMTP Anda
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = "Invoice Pembayaran Konsultasi KiwKiw Petshop"
    body = f"""
==================================================
                JAM GROOMING
==================================================

  Nama                    : {name}
  Jam Konsul              : {waktu_awal}-{waktu_akhir}
  Tanggal                 : {tanggal}

  MOHON DATANG TEPAT WAKTU !

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
        print("----Email dengan invoice Jadwal Grooming telah berhasil dikirim ke email anda!----")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")
    finally:
        server.quit()

def send_invoice_email(name, amount, email):
    smtp_server = "smtp.gmail.com"  # Ganti dengan SMTP server Anda
    smtp_port = 587  # Ganti dengan port SMTP yang sesuai
    smtp_username = "petshopkiwkiw@gmail.com"  # Ganti dengan username SMTP Anda
    smtp_password = "huna bhnh uinc zpgb"  # Ganti dengan password SMTP Anda

    # Membangun Pesan Email
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = "Invoice Pembayaran Konsultasi KiwKiw Petshop"

    # Isi Pesan Email
    body = f"""
    ==================================================
                 INVOICE PEMBAYARAN KONSULTASI
    ==================================================

      Nama Pengguna        : {name}
      Biaya Konsultasi     : Rp{amount}
      Email                : {email}

    ==================================================
    TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KONSULTASI
                     KIW KIW PETSHOP
    ==================================================
    """
    msg.attach(MIMEText(body, 'plain'))

    # Mengirim email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        print("----Email dengan invoice pembayaran konsultasi telah berhasil dikirim!----")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")
    finally:
        server.quit()





