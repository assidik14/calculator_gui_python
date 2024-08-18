import tkinter as tk

# Variabel
expression = ""
input_text = tk.StringVar()

# Fungsi
def klik(tombol):
    '''Fungsi untuk menerima click tombol angka dari user'''
    global expression
    expression = expression + str(tombol)
    input_text.set(expression)

def hapus():
    '''Fungsi untuk membersihkan layar'''
    global expression
    expression = ""
    input_text.set("")

def samadengan():
    '''Fungsi untuk menghitung angka yang di input user'''
    global expression
    hasil = str(eval(expression))
    input_text.set(hasil)
    expression = ""