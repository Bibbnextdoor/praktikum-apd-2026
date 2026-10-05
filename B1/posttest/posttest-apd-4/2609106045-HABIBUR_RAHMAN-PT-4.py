username = "Habib"
password = "045"
luas_per_titik = 5

garis = "-" * 50

print(garis)
print("     SISTEM REKAPITULASI TITIK API KARHUTLA")
print("   BPBD & Manggala Agni  |  Sumber: Satelit BMKG")
print(garis)


while True:
    input_user = input("Username : ")
    input_pass = input("Password : ")

    if input_user == "" or input_pass == "":
        print("Username dan password tidak boleh kosong!")
        print("Masukkan kembali username dan password anda")
    elif input_user.lower() != username.lower() and input_pass != password:
        print("Username dan password salah!")
        print("Masukkan kembali username dan password anda")
    elif input_user.lower() != username.lower():
        print("Username salah!")
        print("Masukkan kembali username dan password anda")
    elif input_pass != password:
        print("Password salah!")
        print("Masukkan kembali username dan password anda")
    else:
        print("Login berhasil. Selamat datang !")
        break

kalimantan_gambut = 0
sumatera_mineral = 0


lagi = "Y"
while lagi == "Y":
    print(garis)
    print("                 INPUT DATA TITIK API")
    print(garis)

    pulau = ""
    while pulau != "KALIMANTAN" and pulau != "SUMATERA":
        pulau = input("Pulau (KALIMANTAN/SUMATERA)  : ").upper()
        if pulau == "":
            print(" Input tidak boleh kosong!")
        elif pulau != "KALIMANTAN" and pulau != "SUMATERA":
            print(" Pulau harus KALIMANTAN atau SUMATERA!")

    if pulau == "KALIMANTAN":
        jenis = ""
        while jenis != "GAMBUT":
            jenis = input("Jenis lahan (GAMBUT)     : ").upper()
            if jenis == "":
                print(" Input tidak boleh kosong!")
            elif jenis != "GAMBUT":
                print(" Lahan Kalimantan hanya GAMBUT!")

        if jenis == "GAMBUT":
            kategori = "Kalimantan-Gambut"
    else:
        jenis = ""
        while jenis != "MINERAL":
            jenis = input("Jenis lahan (MINERAL)        : ").upper()
            if jenis == "":
                print(" Input tidak boleh kosong!")
            elif jenis != "MINERAL":
                print(" Lahan Sumatera hanya MINERAL!")

        if jenis == "MINERAL":
            kategori = "Sumatera-Mineral"


    hotspot = ""
    while not hotspot.isdigit():
        hotspot = input("Jumlah titik api (hotspot)   : ")
        if hotspot == "":
            print(" Input tidak boleh kosong!")
        elif not hotspot.isdigit():
            print(" Masukkan angka bulat positif!")

    hotspot = int(hotspot)
    luas = hotspot * luas_per_titik

    if kategori == "Kalimantan-Gambut":
        kalimantan_gambut += luas
    else:
        sumatera_mineral += luas

    print(garis)
    print(f"[Data diterima] {kategori}: {hotspot} titik api = {luas} Ha lahan rusak")
    print(garis)


    lagi = ""
    while lagi != "Y" and lagi != "T":
        lagi = input("Apakah anda masih mau input data titik api lagi? (Y/T) : ").upper()
        if lagi == "":
            print(" Input tidak boleh kosong!")
        elif lagi != "Y" and lagi != "T":
            print(" Jawaban tidak valid, jawab dengan Y atau T saja!")
    print()

total = kalimantan_gambut + sumatera_mineral

print(garis)
print("        REKAPITULASI TOTAL LUAS LAHAN TERBAKAR")
print(garis)
print(f" Kalimantan - Gambut  : {kalimantan_gambut} Ha")
print(f" Sumatera   - Mineral : {sumatera_mineral} Ha")
print(garis)
print(f" TOTAL KESELURUHAN    : {total} Ha")
print(garis)
print(" Bantuan helikopter water bombing siap dialokasikan.")