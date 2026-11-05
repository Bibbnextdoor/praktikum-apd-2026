users = {
    "admin": {"password": "adminbarca", "role": "admin"},
    "user": {"password": "userbarca", "role": "user"},
}
 
pemain = {
    "1": {"nama": "Lionel Messi", "posisi": "Penyerang", "no": 10},
    "2": {"nama": "Luis Suarez", "posisi": "Penyerang", "no": 9},
    "3": {"nama": "Neymar Jr", "posisi": "Penyerang", "no": 11},
}
 
id_terakhir = 3
 
 
def buat_id_baru():
    global id_terakhir
    id_terakhir += 1
    return str(id_terakhir)
 
 
def hitung_pemain():
    return len(pemain)
 