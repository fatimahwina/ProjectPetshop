from tkinter import *
from tkinter import messagebox
import tkinter as tk 
import csv
import shortcut_pandas as ps

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username entered:", username)
    print("Password entered:", password)
    sukses = False
    with open('C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'r') as file:
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
    
def halaman_login():
    global window
    window = tk.Tk()
    window.title("Login")
    window.geometry("1166x718")
    window.configure(bg="Pink")
    window.resizable(True, True)

    frame = tk.Frame(window, width=350, height=350, bg="White")
    frame.place(x=660, y=200)

    heading = Label(frame, text="Login", fg="#de5d83", bg="White", font=("Candy Beans", 23))
    heading.place(x=135, y=10)

    global username_entry, password_entry
    username_label = Label(frame, text="Username", fg="#de5d83", font=(7))
    username_label.place(x=15, y=50)  # Adjust label position for alignment
    username_entry = Entry(frame, width=20, fg="White", border="2", bg="#de5d83", font=(11))
    username_entry.place(x=110, y=50)  # Adjust entry position for alignment

    password_label = Label(frame, text="Password", fg="#de5d83", font=(7))
    password_label.place(x=15, y=90)  # Adjust label position for alignment
    password_entry = Entry(frame, show="*", width=20, fg="White", border="2", bg="#de5d83", font=(11))
    password_entry.place(x=110, y=90)  # Adjust entry position for alignment

    img = PhotoImage(file="C:\Praktikum prokom\ProjectPetshop\image\kiwkiw 2.png")  # Adjust the image path
    label_gambar = Label(window, image=img, bg="Pink")
    label_gambar.place(x=100, y=200)
    def toggle_password():
        current_show = password_entry.cget("show")
        if current_show == '':
            password_entry.config(show="*")  # Hide password
        else:
            password_entry.config(show="")   # Show password

    show_hide_button = Button(frame, width=7, height=1, text="Show", fg="white", bg="#de5d83", command=toggle_password)
    show_hide_button.place(x=270, y=90)  # Adjust button position for alignment

    Button(frame, width=38, height=1, text="Login", fg="white", bg="#de5d83", command=login).place(x=37, y=155)
    Button(frame, width=38, height=1, text="Register", fg="white", bg="#de5d83", command=halaman_register).place(x=37, y=185)

    window.mainloop()

def signup():
    name = username.get()
    password = user_password.get()
    email = user_email.get()

    if email_form(email):
        # Generate a random OTP
        if email_form(email):
          kode_otp = ps.generate_otp() 
        ps.send_otp_email(email, kode_otp)

        # Send OTP using your preferred method (replace with your implementation)
        # For example, using an email library:
        # send_otp_email(email, kode_otp)

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
                # Write data to login.csv
                with open('C:\Praktikum prokom\ProjectPetshop\data\login.csv', 'a', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, password, email])
                messagebox.showinfo(title="Success", message="Register berhasil, silahkan login")
                otp_window.destroy()  # Close OTP window
            else:
                messagebox.showerror(title="Error", message="Kode OTP tidak valid, silahkan input dengan benar!")

        verify_button = tk.Button(otp_window, text="Verify", command=verify_otp, width=10)
        verify_button.pack(pady=10)
                    
def halaman_register():
    global window_register
    window_register = tk.Tk()
    window_register.title("Register")
    window_register.geometry("1166x718")
    window_register.configure(bg="White")
    window_register.resizable(True,True)
    
    frame = tk.Frame(window_register, width=350, height=350, bg="#de5d83")
    frame.place(x=600,y=200)

    heading = Label(frame,text="Register", fg="White", bg="#de5d83", font=("Candy Beans",23))
    heading.place(x=110,y=15)

    global username, user_password, user_email
    username = Entry(frame, width= 25, fg="#de5d83", border="2", bg="White", font=(11))
    username.place(x=35,y=75)

    user_password = Entry(frame, width= 25, fg="#de5d83", border="2", bg="White", font=(11))
    user_password.place(x=35,y=115)

    user_email = Entry(frame, width= 25, fg="#de5d83", border="2", bg="White", font=(11))
    user_email.place(x=35,y=155)

    # Menambahkan label untuk gambar

    # Define buttons
    Button(frame, width=38, height=1, text="Sign up", fg = "white", bg ="#de5d83", command=signup).place(x=40,y=185) 
    Button(frame, width=10, height=1, text="Back", fg = "Black", border = 0, command=back_login).place(x=0,y=0)

    img = PhotoImage(file="C:\Praktikum prokom\ProjectPetshop\image\kiwkiw 2.png")

    # Place label_gambar after buttons
    label_gambar = Label(window_register, image=img, bg="Pink")
    label_gambar.place(x=100,y=200)

    window_register.mainloop()

def back_login():
    # Hide the registration window instead of destroying it
    window_register.withdraw()

    # Show the login window
    window.deiconify()  # If minimized or hidden
    window.focus_force()  # Bring to front

def email_form(email):
    # Simple email validation function
    if "@" in email and "." in email:
        return True
    return False

halaman_login()