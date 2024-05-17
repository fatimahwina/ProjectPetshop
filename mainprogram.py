import csv
import random
import datetime
import pandas as pd
import shortcut_pandas as ps

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
            login()
            break
        elif option == '2':
            signup()
            break
        else:
            print('Input tidak valid')

# Function for user login
def login():
    global name
    global email_user
    name = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    sukses = False
    with open('login.csv', 'r') as file:
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
            with open('login.csv', 'a', newline="") as file:
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
        with open('Daftar_Produk.csv', 'r', encoding='utf-8') as file:
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
        with open('Daftar_Peralatan.csv', 'r', encoding='utf-8') as file:
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
        pass

    elif option == '4':
        pass

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
            with open("Daftar_Produk.csv", "r") as file:
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
            with open("Daftar_Peralatan.csv", "r") as file:
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
        save_transaction_data(cart, total_price, payment_method, current_time)

        # Display transaction confirmation
        print("\nTransaksi berhasil!")

def save_transaction_data(cart, total_price, payment_method, current_time):
    """Saves transaction data to a CSV file."""
    with open("data_transaksi.csv", "a", newline="") as file:
        writer = csv.writer(file)
        transaction_details = [current_time, ", ".join([item["Nama Produk"] for item in cart]),
                               total_price, payment_method]
        writer.writerow(transaction_details)

# Mulai program
begin ()