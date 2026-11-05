import os
from prettytable import PrettyTable
 
 
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
 
 
def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")
 
 
def header(judul):
    bersihkan_layar()
    tabel = PrettyTable()
    tabel.header = False
    tabel.min_width = 37
    tabel.align = "c"
    tabel.add_row([judul])
    print(tabel)
 
 
def tampil_menu(daftar_menu):
    """daftar_menu: list of tuple (nomor, label)."""
    tabel = PrettyTable(["No", "Menu"])
    tabel.align["Menu"] = "l"
    for nomor, label in daftar_menu:
        tabel.add_row([nomor, label])
    print(tabel)