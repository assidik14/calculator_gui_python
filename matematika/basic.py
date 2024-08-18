# Module perhitungan basic matematika

from operator import sub, truediv
from functools import reduce

def tambah(*args:int)->int:
    '''Fungsi penjumlahan'''
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

def kurang(*args:int)->int:
    '''Fungsi pengurangan'''
    return reduce(sub, args)

def kali(*args:int)->int:
    '''Fungsi perkalian'''
    hasil = 1
    for angka in args:
        hasil *= angka
    return hasil

def bagi(*args:int)->float:
    '''Fungsi pembagian'''
    return reduce(truediv, args)