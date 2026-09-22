makanan_1 = int (15000)
makanan_2 = int (16000)
makanan_3 = int (19000)
makanan_4 = int (20000)
makanan_5 = int (21000)
makanan_6 = int (22000)

harga_makanan = [makanan_1,makanan_2,makanan_3,makanan_4,makanan_5,makanan_6]
biaya_aplikasi = int (5000)
hasil_penjumlahan = int (harga_makanan[0] + harga_makanan[1] + harga_makanan[2] + harga_makanan[3] + harga_makanan[4] + harga_makanan[5])
total_keseluruhan = int (hasil_penjumlahan + biaya_aplikasi)
banyak_data = len(harga_makanan)
rata_rata = int (total_keseluruhan / banyak_data)
nim = int (45)
bolean = nim != rata_rata
total_euro = total_keseluruhan / 20443

print ("Harga makanan : ", (harga_makanan[-6:]))
print ("Total harga sebelum pajak:", hasil_penjumlahan)
print ("Total harga yang harus dibayar: ",total_keseluruhan)
print ("Rata-rata: ", rata_rata)
print ("nim : ", nim)
print ("Output bolean: ", bolean)
print (f"total_euro =  {total_euro:.2f}")
