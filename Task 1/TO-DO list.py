import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.isfile(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_tasks(tasks):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Save error", f"Could not save tasks:\n{e}")


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To‑Do List")

        top_frame = tk.Frame(root)
        top_frame.pack(padx=10, pady=5, fill="x")

        self.entry = tk.Entry(top_frame)
        self.entry.pack(side="left", expand=True, fill="x")
        self.entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(top_frame, text="Add", command=self.add_task)
        add_btn.pack(side="left", padx=(5, 0))

        mid_frame = tk.Frame(root)
        mid_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.listbox = tk.Listbox(mid_frame, selectmode=tk.SINGLE)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(mid_frame, command=self.listbox.yview)
        scrollbar.pack(side="left", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        bottom_frame = tk.Frame(root)
        bottom_frame.pack(padx=10, pady=5, fill="x")

        done_btn = tk.Button(bottom_frame, text="Mark done", command=self.mark_done)
        done_btn.pack(side="left")

        del_btn = tk.Button(bottom_frame, text="Delete", command=self.delete_task)
        del_btn.pack(side="left", padx=(5, 0))

        edit_btn = tk.Button(bottom_frame, text="Edit", command=self.edit_task)
        edit_btn.pack(side="left", padx=(5, 0))

        self.tasks = load_tasks()
        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            text = t["text"]
            if t.get("done"):
                text = "".join(c + "\u0336" for c in text)
            self.listbox.insert(tk.END, text)

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.tasks.append({"text": text, "done": False})
        self.entry.delete(0, tk.END)
        self.refresh_listbox()
        save_tasks(self.tasks)

    def get_selected_index(self):
        sel = self.listbox.curselection()
        if not sel:
            return None
        return sel[0]

    def mark_done(self):
        idx = self.get_selected_index()
        if idx is None:
            return
        self.tasks[idx]["done"] = not self.tasks[idx].get("done", False)
        self.refresh_listbox()
        save_tasks(self.tasks)

    def delete_task(self):
        idx = self.get_selected_index()
        if idx is None:
            return
        confirm = messagebox.askyesno(
            "Delete task", "Are you sure you want to delete the selected task?"
        )
        if confirm:
            self.tasks.pop(idx)
            self.refresh_listbox()
            save_tasks(self.tasks)

    def edit_task(self):
        idx = self.get_selected_index()
        if idx is None:
            return
        old_text = self.tasks[idx]["text"]
        new_text = simpledialog.askstring("Edit task", "Update task:", initialvalue=old_text)
        if new_text is None:
            return
        new_text = new_text.strip()
        if new_text:
            self.tasks[idx]["text"] = new_text
            self.refresh_listbox()
            save_tasks(self.tasks)


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



