from tkinter import *
from tkinter import messagebox
import tkinter as tk
import csv
import shortcut_pandas as ps
from pathlib import Path

# Function to validate email format
def email_form(email):
    if "@" in email and "." in email:
        return True
    return False

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username entered:", username)
    print("Password entered:", password)
    sukses = False
    with open('C:/Praktikum prokom/ProjectPetshop/data/login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = row
            print("Checking:", a, b)
            if username == a and password == b:
                sukses = True
                break

    if sukses:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

# Function to handle registration
def signup():
    name = username_entry_reg.get()
    password = password_entry_reg.get()
    email = email_entry_reg.get()

    if email_form(email):
        # Generate a random OTP
        kode_otp = ps.generate_otp()
        ps.send_otp_email(email, kode_otp)

        otp_window = tk.Tk()
        otp_window.title("Enter OTP")
        otp_window.geometry("300x150")
        otp_window.configure(bg="Pink")
        otp_window.resizable(False, False)

        otp_label = tk.Label(otp_window, text="Masukkan kode OTP:", font=("Arial", 12))
        otp_label.pack(pady=10)

        otp_entry = tk.Entry(otp_window, width=20, font=("Arial", 12))
        otp_entry.pack()

        def verify_otp():
            verif = otp_entry.get()
            if verif == kode_otp:
                with open('C:/Praktikum prokom/ProjectPetshop/data/login.csv', 'a', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, password, email])
                messagebox.showinfo(title="Success", message="Register berhasil, silahkan login")
                otp_window.destroy()  # Close OTP window
                halaman_login()
            else:
                messagebox.showerror(title="Error", message="Kode OTP tidak valid, silahkan input dengan benar!")

        verify_button = tk.Button(otp_window, text="Verify", command=verify_otp, width=10)
        verify_button.pack(pady=10)

# Function to create the login page
def halaman_login():
    global username_entry, password_entry  # Use global to access these variables in login()

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
        font=("Kavoon Regular", 40 * -1)
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
        command=halaman_register
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

# Function to create the registration page
def halaman_register():
    global username, user_password, user_email  # Use global to access these variables in signup()
    
    window_register = Tk()
    window_register.geometry("1166x718")
    window_register.configure(bg="#ACCDFF")

    canvas = Canvas(
        window_register,
        bg="#ACCDFF",
        height=718,
        width=1166,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    
    window_register.image_image_a = PhotoImage(file=relative_to_assets("image_a.png"))
    canvas.create_image(583.0, 359.0, image=window_register.image_image_a)

    window_register.image_image_b = PhotoImage(file=relative_to_assets("image_b.png"))
    canvas.create_image(837.0, 368.0, image=window_register.image_image_b)

    canvas.create_text(
        741.0, 193.0,
        anchor="nw",
        text="Register",
        fill="#FF27A8",
        font=("Kavoon Regular", 40 * -1)
    )

    canvas.create_text(
        696.0, 257.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    username = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    username.place(
        x=707.0, y=275.0,
        width=262.0, height=42.0
    )

    canvas.create_text(
        696.0, 336.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    user_password = Entry(
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

    canvas.create_text(
        696.0, 414.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    user_email = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    user_email.place(
        x=707.0, y=432.0,
        width=262.0, height=42.0
    )

    window_register.button_image_a = PhotoImage(file=relative_to_assets("button_a.png"))
    Button(
        image=window_register.button_image_a,
        borderwidth=0,
        highlightthickness=0,
        command=halaman_login,
        relief="flat"
    ).place(
        x=691.0, y=508.0,
        width=294.0, height=44.0
    )

    window_register.button_image_b = PhotoImage(file=relative_to_assets("button_b.png"))
    Button(
        image=window_register.button_image_b,
        borderwidth=0,
        highlightthickness=0,
        command=signup,
        relief="flat"
    ).place(
        x=691.0, y=453.0,
        width=294.0, height=44.0
    )

    window_register.resizable(False, False)
    window_register.mainloop()

# Function to get the relative path to the assets
def relative_to_assets(path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Praktikum prokom/ProjectPetshop/build/assets/frame0")
    return ASSETS_PATH / Path(path)

# Start the application with the login page
halaman_login()
