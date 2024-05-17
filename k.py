from tkinter import *
from tkinter import messagebox
import tkinter as tk 
import csv

def login():
    username = username_entry.get()
    password = password_entry.get()
    sukses = False
    with open('login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = row
            if username == a and password == b:
                sukses = True
                break

    if sukses:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def halaman_login():
    window = tk.Tk()
    window.title("Login")
    window.geometry("1166x718")
    window.configure(bg="Pink")
    window.resizable(True, True)
    
    frame = tk.Frame(window, width=350, height=350, bg="White")
    frame.place(x=660, y=200)

    heading = Label(frame, text="Login", fg="#de5d83", bg="White", font=("Candy Beans", 23))
    heading.place(x=135, y=10)

    global username_entry
    global password_entry
    username_entry = Entry(frame, width=25, fg="White", border="2", bg="#de5d83", font=(11))
    username_entry.place(x=35, y=75)

    password_entry = Entry(frame, width=25, fg="White", border="2", bg="#de5d83", font=(11))
    password_entry.place(x=35, y=115)

    img = PhotoImage(file="C:\Praktikum prokom\petshop1\petshop\kiwkiw 2.png")

    label_gambar = Label(window, image=img, bg="Pink")
    label_gambar.place(x=100,y=200)

    Button(frame, width=38, height=1, text="Login", fg="white", bg="#de5d83", command=login).place(x=37, y=155) 
    Button(frame, width=38, height=1, text="Register", fg="white", bg="#de5d83", command=halaman_register).place(x=37, y=185) 
    
    window.mainloop()

def halaman_register():
    window = tk.Tk()
    window.title("Register")
    window.geometry("1166x718")
    window.configure(bg="White")
    window.resizable(True,True)
    
    frame = tk.Frame(window, width=350, height=350, bg="#de5d83")
    frame.place(x=600,y=200)

    heading = Label(frame,text="Register", fg="White", bg="#de5d83", font=("Candy Beans",23))
    heading.place(x=110,y=15)

    username = Entry(frame, width= 25, fg="#de5d83", border="2", bg="White", font=(11))
    username.place(x=35,y=75)

    password = Entry(frame, width= 25, fg="#de5d83", border="2", bg="White", font=(11))
    password.place(x=35,y=115)

    img = PhotoImage(file="C:\Praktikum prokom\petshop1\petshop\kiwkiw 2.png")

    label_gambar = Label(window, image=img, bg="Pink")
    label_gambar.place(x=100,y=200)
    
    Button(frame, width=38, height=1, text="Sign up", fg = "white", bg ="#de5d83").place(x=40,y=185) 
    Button(frame, width=10, height=1, text="Back", fg = "Black", border = 0, command=back_login).place(x=0,y=0)

    window.mainloop()

def back_login():
    window.destroy()
    halaman_login()

halaman_login()