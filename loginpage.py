import tkinter as tk
from tkinter import messagebox

def perform_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Trevor" and password == "password123":
        messagebox.showinfo("Login Successful", "Welcome, {}!".format(username))
    else:
        messagebox.showerror("Login Failed!", "Invalid username or password")

root = tk.Tk()
root.title("Login Form")
root.geometry("500x300")

username_label = tk.Label(root, text="Username:", font= ("Arial", 13))
username_label.pack()

username_entry = tk.Entry(root, font=("Arial", 12), width=30)
username_entry.pack()

password_label = tk.Label(root, text="Password:", font=("Arial", 13))
password_label.pack()

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack()

login_button = tk.Button(root, text="Login", command=perform_login)
login_button.pack()

# Bind the Enter key event to the perform_login function
root.bind("<Return>", lambda event=None: perform_login())

root.mainloop()
