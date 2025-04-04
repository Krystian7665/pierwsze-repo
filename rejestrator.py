import tkinter as tk
from tkinter import messagebox
import time
import re

def start_timer():
    global start_time
    start_time = time.time()
    start_button.config(text="Stop", command=stop_timer)

def stop_timer():
    global start_time, end_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_label.config(text=f"Czas trwania: {elapsed_time:.2f} s")
    description_entry.config(state="normal")
    save_button.config(state="normal")
    start_button.config(state="disabled")

def save_entry():
    description = description_entry.get()
    if not validate_description(description):
        messagebox.showerror("Błąd", "Opis zawiera niedozwolone znaki lub jest za długi!")
        return
   
    elapsed_time = end_time - start_time
    entry_text = f"Czas: {time.strftime('%H:%M:%S', time.localtime(start_time))} - {time.strftime('%H:%M:%S', time.localtime(end_time))} (trwanie: {elapsed_time:.2f} s)\nOpis: {description}"
    listbox.insert(tk.END, entry_text)
    reset_ui()

def validate_description(desc):
    return len(desc) <= 500 and not re.search(r'<.*?>', desc)

def reset_ui():
    description_entry.delete(0, tk.END)
    description_entry.config(state="disabled")
    save_button.config(state="disabled")
    start_button.config(text="Start", command=start_timer, state="normal")
    time_label.config(text="Czas trwania: -")

# GUI
root = tk.Tk()
root.title("Rejestrator czasu")

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

time_label = tk.Label(root, text="Czas trwania: -")
time_label.pack()

description_entry = tk.Entry(root, state="disabled", width=50)
description_entry.pack()

save_button = tk.Button(root, text="Zapisz", command=save_entry, state="disabled")
save_button.pack()

listbox = tk.Listbox(root, width=70, height=10)
listbox.pack()

root.mainloop()
