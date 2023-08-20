import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Trevor Mwangi" and password == "passwordis123":
        messagebox.showinfo("Login Success!", "Welcome, Trevor!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

#  main window
window = tk.Tk()
window.title("LOGIN")
window.geometry("500x300")

username_label = tk.Label(window, text="Username:", font=("Arial", 13))
username_label.pack()
username_entry = tk.Entry(window, font=("Arial", 12), width=30)
username_entry.pack()

password_label = tk.Label(window, text="Password:", font=("Arial", 13))
password_label.pack()
password_entry = tk.Entry(window, show="*", font=("Arial", 12), width=30)
password_entry.pack()

#  login button
login_button = tk.Button(window, text="Login", command=login, font=("Arial", 13))
login_button.pack()

window.mainloop()
