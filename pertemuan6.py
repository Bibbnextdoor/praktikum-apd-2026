# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
# hasil = luas_persegi_panjang()
# print ("Luas persegi panjang", hasil)

# #parameter
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# sisi = luas_persegi(int(input("Masukkan sisi persegi : ")))
# print ("Luas persegi", luas_persegi(sisi))

# def pengumuman(nama): 
#     print(f"hai", nama)

# pengumuman("ayam")

#Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"

# #Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)

# data()

def faktorial(n):
    #Base Case: Kondisi fungsi berhenti
    if n == 0 or n == 1:
        return 1
    #Rekursive Case: Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)
#Memanggil fungsi
hasil_faktorial = faktorial(4)
print(f"Hasil dari 4! {hasil_faktorial}")