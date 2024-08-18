# Import tkinter
import tkinter as tk

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("432x405")
window.title("Calculator Python GUI")
window.resizable(False, False)

# Import Variable dan Fungsi
from func_var import input_text, hapus, klik, samadengan

# Frame :
# Input frame dibagian atas untuk meletakkan input box
# Tombol frame dibagian bawah untuk meletakkan tombol-tombol
input_frame = tk.Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side="top")
tombol_frame = tk.Frame(window, width=312, height=272.5, bg="grey")
tombol_frame.pack()

# Komponen :
# Input box
input_box = tk.Entry(input_frame, font=("arial", 27, "bold"), textvariable=input_text, width=50, justify="right", bg="#eee", bd=0)
input_box.grid(row=0, column=0)
input_box.pack(ipady=10)

# Tombol baris pertama
tombol_clear = tk.Button(tombol_frame, text="C", fg="black", width=38, height=3, bd=1, bg="#eee", cursor="hand2", command=hapus).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
tombol_bagi = tk.Button(tombol_frame, text="/", fg="black", width=10, height=3, bd=1, bg="#eee", cursor="hand2", command=lambda: klik("/")).grid(row=0, column=3, padx=1, pady=1)

# Tombol baris kedua
tombol_tujuh = tk.Button(tombol_frame, text="7", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("7")).grid(row=1, column=0, padx=1, pady=1)
tombol_delapan = tk.Button(tombol_frame, text="8", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("8")).grid(row=1, column=1, padx=1, pady=1)
tombol_sembilan = tk.Button(tombol_frame, text="9", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("9")).grid(row=1, column=2, padx=1, pady=1)
tombol_kali = tk.Button(tombol_frame, text="X", fg="black", width=10, height=3, bd=1, bg="#eee", cursor="hand2", command=lambda: klik("*")).grid(row=1, column=3, padx=1, pady=1)

# Tombol baris ketiga
tombol_empat = tk.Button(tombol_frame, text="4", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("4")).grid(row=2, column=0, padx=1, pady=1)
tombol_lima = tk.Button(tombol_frame, text="5", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("5")).grid(row=2, column=1, padx=1, pady=1)
tombol_enam = tk.Button(tombol_frame, text="6", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("6")).grid(row=2, column=2, padx=1, pady=1)
tombol_kurang = tk.Button(tombol_frame, text="-", fg="black", width=10, height=3, bd=1, bg="#eee", cursor="hand2", command=lambda: klik("-")).grid(row=2, column=3, padx=1, pady=1)

# Tombol baris keempat
tombol_satu = tk.Button(tombol_frame, text="1", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("1")).grid(row=3, column=0, padx=1, pady=1)
tombol_dua = tk.Button(tombol_frame, text="2", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("2")).grid(row=3, column=1, padx=1, pady=1)
tombol_tiga = tk.Button(tombol_frame, text="3", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("3")).grid(row=3, column=2, padx=1, pady=1)
tombol_tambah = tk.Button(tombol_frame, text="+", fg="black", width=10, height=3, bd=1, bg="#eee", cursor="hand2", command=lambda: klik("+")).grid(row=3, column=3, padx=1, pady=1)

# Tombol baris kelima
tombol_nol = tk.Button(tombol_frame, text="0", fg="black", width=24, height=3, bd=1, bg="#fff", cursor="hand2", command=lambda: klik("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tombol_titik = tk.Button(tombol_frame, text=".", fg="black", width=10, height=3, bd=1, bg="#eee", cursor="hand2", command=lambda: klik(".")).grid(row=4, column=2, padx=1, pady=1)
tombol_samadengan = tk.Button(tombol_frame, text="=", fg="black", width=10, height=3, bd=1, bg="#eee", cursor="hand2", command=samadengan).grid(row=4, column=3, padx=1, pady=1)

# Mainloop Window
window.mainloop()