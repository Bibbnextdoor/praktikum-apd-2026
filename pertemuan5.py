# kartu = ("kartu merah, kartu merah, kartu ijo, kartu biru")
# kartuku = set(kartu)
# print(kartuku)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# buah = {"apel", "mangga", "jeruk"}
# buah.remove("mangga")
# print(buah)

# angka1 = {1, 2, 3}
# angka2 = {3, 5, 6}
# angka3 = {"hmmmz"}
# angka2.update(angka3)
# print(angka1)

# praktikum = {
#     "apd" : "belajar dictionary", 
#     "orsikom : "belajar logism"


# }

# Matkul = {
# "Matkul_ganjil" : "kalkulus",
# "Matkul_genap" : "statistik"
# }
# print(Matkul["Matkul_ganjil"])
# print(Matkul)

Biodata = {
"Nama" : "raavfy",
"NIM" : 2609106045,
"KRS" : ["Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Instagram" : "ayambakar"
}

# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat", "alamat tidak ditemukan"))

# print(f"Nama saya adalah {Biodata['Nama']}")
# print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} {Biodata['KRS'][1]}")

# List_game = dict(Genshin_Impact="Open World", Mole="Moba",
# Stardew_Valley="Farming Simulation")
# print(List_game)

# for i in Biodata:
#     print(i)

# for i in Biodata.keys():
#     print(i)

# for i in Biodata.values():
#     print(i)

#     for i, j in Biodata.items():
#         print(f'{i}: {j}')
    
# Biodata["matkul"] = "kalkulus" 
# print(Biodata)

# Biodata.update()

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))
# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# print(game)
# game["valorant"] = "burik"
# print(game)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# print(game)
# game.update({"genshin impact" : "adventure"})
# print(game)
# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# aset.clear()
# print(aset)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print("Panjang dictionary :", len(aset))

# menu = {
# "ayam geprek" : 15000,
# "ayam goreng" : 13000,
# "ayam bakar" : 17000,
# "nasi goreng" : 12000,
# "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# menu_baru["nasi goreng"] = 15000
# print(menu)
# print(menu_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)
# print(menu)

menu = {
"ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
"nasi" : ["nasi goreng", "nasi uduk"],
"mie" : ["mie goreng rendang", "mie goreng aceh"],
"kuah" : ["soto", "rawon", "sop iga"]
}
for i, j in menu.items():
    print(f"Kategori {i} memiliki menu: {j} ")
for kategori in j:
    print(kategori)
print("")
