# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
#     print(f"Total Perulangan : {hitung}")

# for i in range(10):
#         if i == 9:
#             break
#         print(i)

# for i in range(50):
#         if i > 9:
#             break
#         print("ayam goreng", i)

angka_benar = 7

while True:
    print("=== Game Tebak Angka ===")


    angka_input = int(input("Masukkan angka (1-10) : "))


    if angka_benar == angka_input:
        print("Angka yang kamu masukkan benar")
        break
    else:
        print("Angka masih salah")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
