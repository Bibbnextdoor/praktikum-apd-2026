print("Selamat datang di ANGKASA, Aplikasi streaming musik supermantap dan terbaik 1 Indonesia ")

nama_sesuai = "Habibur"
nim_sesuai = "45"  
 
biaya_langganan = 1500000
 
nama = input("Masukkan Nama: ")
nim = input("Masukkan Nim: ")
 
if nama == nama_sesuai and nim == nim_sesuai:
    
    print("Login berhasil, Selamat datang di ANGKASA !,", nama)
    print("Dengarkan musikmu, Nikmati setiap momennya")
    print("Jangan biarkan akses yang terbatas mengganggu momen mu, Ayo berlangganan sekarang !")
 
    print("Pilih paket langganan anda untuk pengalaman yang lebih maksimal:")
    print("1. Orbit     (biaya administrasi 1%) - akses dasar ke lagu-lagu populer")
    print("2. Nebula    (biaya administrasi 3%) - akses lagu premium dan playlist kustom")
    print("3. Galaxy    (biaya administrasi 5%) - akses lagu premium, playlist kustom, dan mode offline ")
    print("4. Supernova (biaya administrasi 7%) - akses lagu premium, playlist kustom, mode offline, dan konten eksklusif artis")
 
    pilihan = input("Masukkan pilihan paket anda (1/2/3/4): ")


 
    if pilihan == "1":
        nama_paket = "Orbit"
        biaya_administrasi = 0.01
        fitur = "akses dasar ke lagu-lagu populer"
    elif pilihan == "2":
        nama_paket = "Nebula"
        biaya_administrasi = 0.03
        fitur = "akses lagu premium & playlist kustom"
    elif pilihan == "3":
        nama_paket = "Galaxy"
        biaya_administrasi = 0.05
        fitur = "akses lagu premium, playlist kustom, dan mode offline"
    elif pilihan == "4":
        nama_paket = "Supernova"
        biaya_administrasi = 0.07
        fitur = "akses lagu premium, playlist kustom, mode offline, dan konten eksklusif artis"
    else:
        nama_paket = None
 
    if nama_paket:
        biaya_administrasi = round (biaya_langganan * biaya_administrasi)
        total_biaya = biaya_langganan + biaya_administrasi
 
        print("     STRUK PEMBAYARAN    ")
        print("Paket        :", nama_paket)
        print("Biaya administrasi  : Rp", format(biaya_administrasi, ",").replace(",", "."))
        print("Total biaya  : Rp", format(total_biaya, ",").replace(",", "."))
        print("Fitur        :", fitur)
        print("Terima kasih sudah berlangganan, Anda memilih aplikasi yang tepat !")
        
    else:
        print(  "Pilihan tidak tersedia."  )
else:
    print("  Login gagal! Nama atau nim salah, Masukkan kembali nama dan nim anda   ")
 
 

