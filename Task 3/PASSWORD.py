import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return
        
        characters = ""
        if var_lower.get(): characters += string.ascii_lowercase
        if var_upper.get(): characters += string.ascii_uppercase
        if var_numbers.get(): characters += string.digits
        if var_symbols.get(): characters += string.punctuation
        
        if characters == "":
            messagebox.showwarning("Warning", "Select at least one character type")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")


root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")

tk.Label(root, text="Strong Password Generator", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack(pady=5)

var_lower = tk.BooleanVar()
var_upper = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Lowercase Letters (a-z)", variable=var_lower).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Uppercase Letters (A-Z)", variable=var_upper).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Numbers (0-9)", variable=var_numbers).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Symbols (! @ # $ %)", variable=var_symbols).pack(anchor="w", padx=30)

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 14), command=generate_password)
generate_btn.pack(pady=15)

result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
