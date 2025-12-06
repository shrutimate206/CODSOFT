import tkinter as tk
from tkinter import messagebox

def btn_click(value):
    current = display.get()
    if current == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)
    display.insert(0, "0")

def delete():
    current = display.get()
    if len(current) > 1:
        display.delete(len(current)-1, tk.END)
    else:
        display.delete(0, tk.END)
        display.insert(0, "0")

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero")
    except:
        messagebox.showerror("Error", "Invalid Expression")

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("420x550")
root.configure(bg="#1e1e1e")

display = tk.Entry(
    root, font=("Arial", 32),
    bd=10, bg="#000", fg="#0f0",
    justify="right"
)
display.insert(0, "0")
display.pack(fill="both", pady=10, padx=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

buttons = [
    ["C", "DEL", "/", "*"],
    ["7", "8", "9", "-"],
    ["6", "5", "4", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""]
]

def create_button(text):
    if text == "":
        return tk.Label(frame, bg="#1e1e1e")

    style = {"font": ("Arial", 18), "fg": "white", "bd": 1}

    if text == "C":
        return tk.Button(frame, text=text, bg="#ff3b30", command=clear, **style)
    elif text == "DEL":
        return tk.Button(frame, text=text, bg="#ff9500", command=delete, **style)
    elif text == "=":
        return tk.Button(frame, text=text, bg="#34c759", command=calculate, **style)
    else:
        return tk.Button(frame, text=text, bg="#333", command=lambda v=text: btn_click(v), **style)

for r, row in enumerate(buttons):
    frame.rowconfigure(r, weight=1)
    for c, text in enumerate(row):
        frame.columnconfigure(c, weight=1)
        btn = create_button(text)
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

root.mainloop()
