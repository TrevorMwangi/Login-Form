import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

#Password generator
def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    if not any([use_lowercase, use_uppercase, use_digits, use_special_chars]):
        messagebox.showerror("Error", "Please select at least one option.")
        return

    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    generated_password = "".join(random.choice(chars) for _ in range(length))
    new_password_entry.delete(0, tk.END)  # Clear previous content
    new_password_entry.insert(0, generated_password)

def open_password_generator():
    login_frame.pack_forget()  # Hide the login frame
    password_generator_frame.pack()  # Show the password generator frame

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


#Login Function
def perform_login():
    username = username_entry.get()
    entered_password = password_entry.get()

    if username == "user":
        if entered_password == current_password or entered_password == new_password_entry.get():
            messagebox.showinfo("Login Successful", "Welcome, {}!".format(username))
            root.quit()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    else:
        messagebox.showerror("Login Failed", "Invalid username")


#Main Window Frame
root = tk.Tk()
root.title("Login Form")
root.geometry("500x400")

style = ttk.Style()
custom_font = ("Helvetica", 12)  # Tuple containing font family and size
style.configure("Custom.TButton", font=custom_font)


# Login Frame
login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)

username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

username_entry = tk.Entry(login_frame, font=("Arial", 14))
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14))
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
password_entry.grid(row=1, column=1, padx=10, pady=5,)

show_password_var = tk.BooleanVar()
show_password_check = ttk.Checkbutton(login_frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_check.grid(column=1, row=2, columnspan=2, sticky="W")


login_button = ttk.Button(login_frame, text="Login", command=perform_login, style="Custom.TButton")
login_button.grid(row=6, columnspan=4, padx=20, pady=20)

password_generator_button = ttk.Button(login_frame, text="Forgot Password?", command=open_password_generator)
password_generator_button.grid(row=4, columnspan=2, padx=10, pady=10)

current_password = "password"  # The existing password


# Password Generator Frame
password_generator_frame = tk.Frame(root)

length_label = tk.Label(password_generator_frame, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(password_generator_frame, font=("Arial", 13))
length_entry.pack()

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(password_generator_frame, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack(pady=5, anchor="w")

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(password_generator_frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(pady=5, anchor="w")

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(password_generator_frame, text="Include Digits", variable=digits_var)
digits_check.pack(pady=5, anchor="w")

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(password_generator_frame, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack(pady=5, anchor="w")

generate_button = ttk.Button(password_generator_frame, text="Generate Password", command=generate_password, style="Custom.TButton")
generate_button.pack(pady=10)

new_password_label = tk.Label(password_generator_frame, text="Generated Password:")
new_password_label.pack(pady=5)

new_password_entry = tk.Entry(password_generator_frame, show="", font=("Arial", 12))  # Show generated password
new_password_entry.pack()

back_button = ttk.Button(password_generator_frame, text="Back to Login", command=lambda: [password_generator_frame.pack_forget(), login_frame.pack()], style="Custom.TButton")
back_button.pack(pady=10, padx=10)

new_password = ""  # Initialize the new password

login_frame.pack()  # Display the login frame initially

root.bind("<Return>", lambda event=None: perform_login())
root.mainloop()
