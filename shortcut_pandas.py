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
    with open('C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return row[2]  # Mengembalikan email dari baris yang sesuai dengan username
    return None  # Jika username tidak ditemukan

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





