import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

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
    password_entry.delete(0, tk.END)  # Clear previous content
    password_entry.insert(0, generated_password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x300")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, font = ("Arial", 13))
length_entry.pack(padx=10)

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack(padx=20, anchor="w")

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(padx=20, anchor="w")

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(padx=20, anchor="w")

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack(padx=20, anchor="w")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root, font = ("Arial", 18), show="")  # Show generated password
password_entry.pack()

root.mainloop()
