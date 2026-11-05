from prettytable import PrettyTable
from data import pemain, buat_id_baru, hitung_pemain
from utils import input_angka
 
 
def tampil_pemain():
    tabel = PrettyTable(["ID", "Nama", "Posisi", "No Punggung"])
    tabel.align["Nama"] = "l"
    tabel.align["Posisi"] = "l"
    for id_p, data in pemain.items():
        tabel.add_row([id_p, data["nama"], data["posisi"], data["no"]])
    print(tabel)
    print(f"Total pemain: {hitung_pemain()}")
 
 
def tambah_pemain():
    nama = input("Nama: ")
    posisi = input("Posisi: ")
    try:
        assert nama != "" and posisi != "", "Data tidak boleh kosong!"
    except AssertionError as e:
        print(e)
        return
    no = input_angka("No punggung: ")
    pemain[buat_id_baru()] = {"nama": nama, "posisi": posisi, "no": no}
    print("Pemain berhasil ditambahkan")
 
 
def ubah_pemain():
    id_user = input("Masukkan ID pemain: ")
    try:
        data = pemain[id_user]
    except KeyError:
        print("ID tidak ditemukan!")
        return
    print("Kosongkan data yang tidak ingin diubah")
    nama = input("Nama baru: ")
    posisi = input("Posisi baru: ")
    no = input("No punggung baru: ")
    try:
        if no != "":
            data["no"] = int(no)
    except ValueError:
        print("No punggung harus angka!")
        return
    if nama != "":
        data["nama"] = nama
    if posisi != "":
        data["posisi"] = posisi
    print("Data berhasil diubah")
 
 
def hapus_pemain():
    hapus_id = input("Masukkan ID pemain: ")
    try:
        del pemain[hapus_id]
        print("Pemain berhasil dihapus")
    except KeyError:
        print("ID tidak ditemukan!")