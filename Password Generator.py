import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length should be greater than 0.")
        else:
            password = generate_password(length)
            password_display.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create labels, entry, and button widgets
length_label = tk.Label(window, text="Desired Password Length:")
length_entry = tk.Entry(window)
generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked, bg="orange", fg="white")
password_display = tk.Label(window, text="", wraplength=300)

# Organize widgets using grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
password_display.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the GUI main loop
window.mainloop()