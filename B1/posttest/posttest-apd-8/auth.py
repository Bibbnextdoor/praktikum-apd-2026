import pwinput
from data import users
 
 
def cek_login(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return ""
 
 
def input_login():
    username = input("Username: ")
    password = pwinput.pwinput("Password: ", mask="*")
    return username, password
 
 
def register():
    user_baru = input("Username baru: ")
    pass_baru = pwinput.pwinput("Password baru: ", mask="*")
    try:
        assert user_baru != "" and pass_baru != "", "Username dan password tidak boleh kosong!"
        assert user_baru not in users, "Username sudah dipakai!"
        assert len(pass_baru) >= 3, "Password minimal 3 karakter!"
    except AssertionError as e:
        print(e)
        return
    users[user_baru] = {"password": pass_baru, "role": "user"}
    print("Register berhasil, silakan login")