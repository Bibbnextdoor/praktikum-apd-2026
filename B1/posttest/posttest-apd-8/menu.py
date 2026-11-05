from utils import header, tampil_menu
from crud_pemain import tampil_pemain, tambah_pemain, ubah_pemain, hapus_pemain
 
 
def menu_pengguna(role):
    while True:
        header("Menu " + role)
        daftar = [("1", "Lihat pemain")]
        if role == "admin":
            daftar += [
                ("2", "Tambah pemain"),
                ("3", "Ubah pemain"),
                ("4", "Hapus pemain"),
            ]
        daftar.append(("0", "Logout"))
        tampil_menu(daftar)
        menu = input("Pilih menu: ")
 
        if menu == "0":
            break
        elif menu == "1":
            tampil_pemain()
        elif menu == "2" and role == "admin":
            tambah_pemain()
        elif menu == "3" and role == "admin":
            ubah_pemain()
        elif menu == "4" and role == "admin":
            hapus_pemain()
        else:
            print("Pilihan tidak valid!")
        input("Kembali ke menu, tekan enter")