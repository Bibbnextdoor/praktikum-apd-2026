# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print(formula1)

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit.append("Spa-Francorchamps")
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay', 'Spa-Francorchamps']

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit.extend(["Spa-Francorchamps", "Interlagos"])
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay', 'Spa-Francorchamps',
# 'Interlagos']

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit.insert(2, "Interlagos")
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Interlagos', 'Silverstone', 'Marina Bay']

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit[1] = "Monza Italia"
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza Italia', 'Silverstone', 'Marina Bay']

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit[0:2] = ["Sepang", "Mugello"]
# print(sirkuit)
# # Output
# ['Sepang', 'Mugello', 'Silverstone', 'Marina Bay']

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# del sirkuit[2]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Marina Bay']

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# sirkuit.remove("Suzuka")
# print(sirkuit)
# # Output
# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)
# # Output
# ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# ambil_sirkuit = sirkuit.pop(1)

# driver = ["Hamilton", "Verstappen", "Leclerc", "Sainz", "Russell",
# "Antoneli", "Norris"]
# print(driver[0:6:2])

# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]
# gabung_team = team1 + team2
# print(gabung_team)

# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 3
# print(juara)

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]

# for i in line_up:
#     for j in i:
#         print(j, end=' ') 

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# print (chara[4])

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# listchara.append("Yui ")
# chara = tuple(listchara)
# print(chara)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# listchara = list(chara)
# # listchara.extend(["Kohaku", "Deepta"])
# # chara = tuple(listchara)
# # print(chara)

# # chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# # listchara = list(chara)
# listchara.insert(2, "Senku")
# chara = tuple(listchara)
# print(chara)
# # Output
# ('Yukari', 20, 'Senku', True, 150.4, ['Odette', 25], ('Yukino', 22))

# chara = ("Yukari", "Yukino", "Odette", "Senku")
# (Persona, Oregairu, *Ayamgoreng) = chara
# print(Oregairu)
# print(Ayamgoreng)

data_harian = ["Senin", 36.5, "Selasa", 37.1, "Rabu", 36.8, "Kamis", 37.0, "Jumat", 36.6]
print (data_harian[1:11:2])

profil_karakter = ("Arthur", 50, True, ["Pedang Suci", "Tameng Naga"])
print (profil_karakter[::-1])