import csv
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
def begin():
    print("=" * 50)
    print("\n          SELAMAT DATANG DI KIWKIW PETSHOP\n")
    print("=" * 50)
    print("Ketik '1' jika anda sudah ingin Login")
    print("Ketik '2' untuk mendaftar")
    print("=" * 50)
    while True:
        option = input("Silahkan masukkan: ")
        if option == '1':
            clear_screen()
            login()
            break
        elif option == '2':
            signup()
            break
        else:
            print('Input tidak valid')
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
# Function for user login
def login():
    global name
    global email_user
    name = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    sukses = False
    with open(r'C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = row
            if a == name and b == password:
                sukses = True
                break

    if sukses == True:
        print("=" * 50)
        print("LOGIN BERHASIL")
        print("=" * 50)
        email_user = ps.get_email_by_username(name)
        menu()
    else:
        print("=" * 50)
        print("Username atau Password yang anda masukkan salah")
        print("=" * 50)
        login()

# Function for user registration
def signup():
    print("\nMasukkan data diri anda!")
    name = input("Masukkan Username Baru: ")
    password = input("Masukkan Password Baru: ")
    email = input("Masukkan Email Baru: ")
    if email_form(email):
        pass
    else:
        print("\nAlamat email tidak valid. Silakan coba lagi.")
        signup()

    # Generate OTP
    kode_otp = ps.generate_otp()  # Menghasilkan OTP baru

    # Send OTP via email
    ps.send_otp_email(email, kode_otp)

    while True:
        verif = input('Masukkan kode OTP Registrasi yang dikirim ke email anda: ')
        if verif == kode_otp:
            print("=" * 50)
            print("Register berhasil, silahkan login")
            print("=" * 50)
            with open(r'C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'a', newline="") as file:
              writer = csv.writer(file)
              writer.writerow([name, password, email])
            begin()
            break
        else:
            print("Kode OTP tidak valid, silahkan input dengan benar!\n")

# Function to validate email format
def email_form(email):
    # Simple email validation function
    if "@" in email and "." in email:
        return True
    return False
# Function to display the main menu and handle user choices
def menu():
    global opsi_transaksi
    print('\nSelamat datang di menu utama KiwKiw Petshop!')
    print("Ketik '1' Pembelian makanan dan vitamin")
    print("Ketik '2' Pembelian peralatan hewan")
    print("Ketik '3' Layanan")
    print("Ketik '4' Print Out Transaksi")
    print("Ketik '5' Keluar")
    option = input("\nPilih menu : ")


    if option == '1':
        opsi_transaksi = 1
        with open(r'C:\Praktikum prokom\ProjectPetshop\data\Daftar_Produk.csv.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
        for row in data:
            formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
            print('='*83)
            print(formatted_row)
        print('='*83)
        process_purchase()

    elif option == '2':
        opsi_transaksi = 2
        with open(r'C:\Praktikum prokom\ProjectPetshop\data\Daftar_Peralatan.csv.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
        for row in data:
            formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
            print('='*83)
            print(formatted_row)
        print('='*83)
        transaksi_peralatan()

    elif option == '3':
        layanan ()

    elif option == '4':       
        pdf_filename = generate_transaction_pdf(email_user)
        if pdf_filename:
            send_email_with_pdf(email_user, pdf_filename)


    elif option == '5':
        print("\nTerima kasih telah menggunakan KiwKiw Petshop!")

    else:
        print("Pilihan tidak valid. Silakan pilih menu")
        
def process_purchase():
    """Simulates a purchase process with CSV data and payment options."""
    cart = []
    total_price = 0
    while True:
        product_id = input("\nMasukkan ID produk yang ingin dibeli (ketik 'selesai' untuk selesai): ")

        if product_id.lower() == "selesai":
            break

        try:
            product_id = int(product_id)
        except ValueError:
            print("ID produk harus berupa angka. Silakan coba lagi.")
            continue

        if 1 <= product_id <= 10:
            # Load product data from CSV
            with open(r"C:\Praktikum prokom\ProjectPetshop\data\Daftar_Produk.csv", "r") as file:
                reader = csv.reader(file)
                # Skip the header row
                next(reader)
                for row in reader:
                    if int(row[0]) == product_id:
                        product_name, price, stock = row[1:]
                        break

            # Add product to cart and update total price
            if int(stock) > 0:
                cart.append({"id": product_id, "Nama Produk": product_name, "Harga": int(price)})
                total_price += int(price)
                stock = int(stock) - 1
                print(f"Produk {product_name} ditambahkan ke keranjang. Stok tersisa: {stock}.")
            else:
                print(f"Produk {product_name} habis stok.")
        else:
            print("ID produk tidak valid. Silakan pilih antara 1 dan 10.")

def transaksi_peralatan():
    cart = []
    total_price = 0
    while True:
        product_id = input("\nMasukkan ID produk yang ingin dibeli (ketik 'selesai' untuk selesai): ")

        if product_id.lower() == "selesai":
            break

        try:
            product_id = int(product_id)
        except ValueError:
            print("ID produk harus berupa angka. Silakan coba lagi.")
            continue

        if 1 <= product_id <= 10:
            # Load product data from CSV
            with open(r"C:\Praktikum prokom\ProjectPetshop\data\Daftar_Peralatan.csv", "r") as file:
                reader = csv.reader(file)
                # Skip the header row
                next(reader)
                for row in reader:
                    if int(row[0]) == product_id:
                        product_name, price, stock = row[1:]
                        break

            # Add product to cart and update total price
            if int(stock) > 0:
                cart.append({"id": product_id, "Nama Produk": product_name, "Harga": int(price)})
                total_price += int(price)
                stock = int(stock) - 1
                print(f"Produk {product_name} ditambahkan ke keranjang. Stok tersisa: {stock}.")
            else:
                print(f"Produk {product_name} habis stok.")
        else:
            print("ID produk tidak valid. Silakan pilih antara 1 dan 10.")

    # Display cart summary and total price
    if cart:
        print("\nRingkasan Pesanan:")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Waktu Pesanan: {current_time}")
        for item in cart:
            print(f"- {item['Nama Produk']}: Rp{item['Harga']:,}")
        print(f"\nTotal Harga: Rp{total_price:,}")

        # Payment method selection
        payment_method = input("\nPilih metode pembayaran (tunai/non-tunai): ")
        while payment_method.lower() not in ["tunai", "non-tunai"]:
            payment_method = input("Metode pembayaran tidak valid. Pilih 'tunai' atau 'non-tunai': ")

        # Process payment (simulated)
        if payment_method == "tunai":
            print("\nPembayaran tunai diterima.")
        else:
            email_address = input("\nMasukkan alamat email untuk menerima instruksi pembayaran: ")
            print(f"Email instruksi pembayaran telah dikirim ke {email_address}.")

        # Save transaction data to CSV
        save_transaction_data(cart, total_price, payment_method, current_time, email_user)

        # Display transaction confirmation
        print("\nTransaksi berhasil!")

def save_transaction_data(cart, total_price, payment_method, current_time, email_user):
    """Saves transaction data to a CSV file."""
    with open(r"C:\Praktikum prokom\ProjectPetshop\data\data_transaksi.csv", "a", newline="") as file:
        writer = csv.writer(file)
        transaction_details = [current_time, ", ".join([item["Nama Produk"] for item in cart]),
                               total_price, payment_method, email_user]
        writer.writerow(transaction_details)
def layanan():
    print("\nPilih Layanan yang tersedia:")
    print("Ketik '1' untuk Grooming")
    print("Ketik '2' untuk Konsultasi")
    option = input("\nPilih layanan : ")

    if option == '1':
        jadwal_grooming()
    elif option == '2':
        konsultasi()
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

def jadwal_grooming():
    print("--JADWAL BUKA KIW KIW PETSHOP--\n")
    print("       08.00 - 15.00          \n")
    def struk_grooming(name, email):
        ps.struk_konsultasi(name, email,tanggal,waktu_awal, waktu_akhir)    
    
    print("\nMasukkan Tanggal dan Waktu Grooming Anda:")
    
    tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ")
    waktu_awal = input("Masukkan waktu mulai (format: HH:MM): ")
    waktu_akhir = input("Masukkan waktu selesai (format: HH:MM): ")
    
    try:
        datetime.datetime.strptime(tanggal, '%Y-%m-%d')
        datetime.datetime.strptime(waktu_awal, '%H:%M')
        datetime.datetime.strptime(waktu_akhir, '%H:%M')
    except ValueError:
        print("Format tanggal atau waktu tidak valid. Silakan coba lagi.")
        return

    waktu_buka = datetime.time(8, 0)  # Waktu buka petshop
    waktu_tutup = datetime.time(15, 0)  # Waktu tutup petshop
    clear_screen()
    struk_grooming(name, email_user)
    if waktu_awal >= waktu_akhir:
        print("Waktu mulai harus sebelum waktu selesai. Silakan coba lagi.")
        return

    if not (waktu_buka <= datetime.datetime.strptime(waktu_awal, '%H:%M').time() < waktu_tutup):
        print("Grooming hanya tersedia dari jam 8 pagi sampai 3 sore. Silakan pilih waktu di antara waktu tersebut.")
        return

    if not (waktu_buka <= datetime.datetime.strptime(waktu_akhir, '%H:%M').time() < waktu_tutup):
        print("Grooming hanya tersedia dari jam 8 pagi sampai 3 sore. Silakan pilih waktu di antara waktu tersebut.")
        return

    print("\nJadwal Grooming Anda:")
    print(f"Tanggal: {tanggal}")
    print(f"Waktu: {waktu_awal} - {waktu_akhir}")
    balik = input("\n\nApakah anda ingin menggunakan layanan kami Lagi (1/0)?\n(1 = iya, 0 = tidak) : ")
    if  balik == '1':
        return menu()
    elif balik == '2':
        pass

openai.api_key = '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'
#Fungsi memanggil chatgpt AI
def get_ai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content'].strip()

def konsultasi():
    print("Biaya konsultasi adalah Rp100.000,-")
    print("Silakan membayar untuk memulai konsultasi.")
    sudah = input("Ketik 1 jika sudah membayar (0 jika cancel): ")
    clear_screen()
    if sudah == '0' :
        print("TERIMAKASIH TELAH MENGGUNAKAN JASA KONSULTASI KAMI")
    elif sudah == '1':
        print("-------------------------------------------------")
        pertanyaan = input("Silakan ketik pertanyaan Anda: ")

        print("\nPertanyaan:", pertanyaan)
        print("Konsultan Menjawab...\n")
        answer = get_ai_response(pertanyaan)
        print("Jawaban Konsultan :", answer)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def process_non_tunai_payment(name, email):
    amount = 100000
    ps.send_invoice_email(name, amount, email)
    balik = input("\n\nApakah anda ingin menggunakan layanan kami Lagi(1/0)?\n(1 = iya, 0 = tidak) : ")
    if  balik == '1':
        return menu()
    elif balik == '2':
        pass
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
    with open(r'data/data_beli_peralatan.csv', 'r') as file:
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

def generate_transaction_pdf(email_user):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.cell(200, 10, txt="Laporan Transaksi Grooming KiwKiw Petshop", ln=True, align='C')
    pdf.ln(10)

    # Table Header
    pdf.cell(40, 10, txt="Tanggal", border=1)
    pdf.cell(80, 10, txt="Produk", border=1)
    pdf.cell(30, 10, txt="Total Harga", border=1)
    pdf.cell(40, 10, txt="Metode Pembayaran", border=1)
    pdf.ln()

    # Read transaction data
    transactions = []
    with open(r'data/data_riwayat_grooming.csv', 'r') as file:
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
        print("Email dengan laporan transaksi telah berhasil dikirim ke email anda!")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")
    finally:
        server.quit()

begin ()