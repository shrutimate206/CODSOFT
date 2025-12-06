import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

CONTACT_FILE = "contacts.json"
contacts = []


def save_to_json():
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def load_from_json():
    global contacts
    if os.path.exists(CONTACT_FILE):
        try:
            with open(CONTACT_FILE, "r") as f:
                contacts = json.load(f)
        except:
            contacts = []
    else:
        contacts = []


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone Number are required")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_to_json()
    update_contact_list()
    clear_fields()


def update_contact_list():
    listbox.delete(*listbox.get_children())
    for i, contact in enumerate(contacts):
        listbox.insert("", "end", iid=i, values=(contact["name"], contact["phone"]))


def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone:")
    if not query:
        return
    listbox.delete(*listbox.get_children())
    for i, c in enumerate(contacts):
        if query.lower() in c["name"].lower() or query in c["phone"]:
            listbox.insert("", "end", iid=i, values=(c["name"], c["phone"]))


def delete_contact():
    try:
        selected = listbox.selection()[0]
        del contacts[int(selected)]
        save_to_json()
        update_contact_list()
    except:
        messagebox.showwarning("Warning", "Select a contact to delete")


def update_contact():
    try:
        selected = listbox.selection()[0]
        index = int(selected)

        contacts[index]["name"] = entry_name.get()
        contacts[index]["phone"] = entry_phone.get()
        contacts[index]["email"] = entry_email.get()
        contacts[index]["address"] = entry_address.get()

        save_to_json()
        update_contact_list()
        clear_fields()
    except:
        messagebox.showwarning("Warning", "Select a contact to update")


def load_selected(event):
    try:
        selected = listbox.selection()[0]
        index = int(selected)
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contacts[index]["name"])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contacts[index]["phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contacts[index]["email"])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contacts[index]["address"])
    except:
        pass


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Manager")
root.geometry("550x500")

tk.Label(root, text="Contact Management System", font=("Arial", 18)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Phone:").grid(row=1, column=0)
entry_phone = tk.Entry(frame, width=30)
entry_phone.grid(row=1, column=1)

tk.Label(frame, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=2, column=1)

tk.Label(frame, text="Address:").grid(row=3, column=0)
entry_address = tk.Entry(frame, width=30)
entry_address.grid(row=3, column=1)

tk.Button(root, text="Add Contact", width=15, command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", width=15, command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=15, command=delete_contact).pack(pady=5)
tk.Button(root, text="Search Contact", width=15, command=search_contact).pack(pady=5)

listbox = ttk.Treeview(root, columns=("Name", "Phone"), show="headings")
listbox.heading("Name", text="Name")
listbox.heading("Phone", text="Phone")
listbox.pack(pady=10, fill="both")

listbox.bind("<<TreeviewSelect>>", load_selected)

load_from_json()
update_contact_list()

root.mainloop()
