# Import Package
# import matematika
import tkinter as tk
from tkinter import ttk

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x300")
window.title("Calculator Python")
window.resizable(False, False)

# Frame
input_frame = ttk.Frame(window, width=60, height=60)
input_frame.pack_propagate(0)
input_frame.pack(padx=10, pady=10, fill="x", side="top", anchor="w")

# Komponen :
# Input box
input_number = ttk.Entry(input_frame, font=("arial", 24))
input_number.pack(padx=10, pady=10, fill="x", expand=True)

# Mainloop Window
window.mainloop()