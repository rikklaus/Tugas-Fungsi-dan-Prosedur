# Nama: Erik Klaus Keifas Kalalo
# Kelas: 1A
# NIM: 2400887

def cek_password(password):
    return password == "latihan"

def tampilkan_pesan_berhasil():
    print("Selamat datang di aplikasi Dasar Pemrograman")

def tampilkan_pesan_gagal(kesempatan):
    print(f"Login salah! Kesempatan anda {kesempatan} kali lagi")

def tampilkan_pesan_akses_ditolak():
    print("Anda tidak diperkenankan mengakses aplikasi ini")

def login():
    print("Silakan Login")
    print("Login dengan 3 Kesempatan")
    
    for kesempatan in range(3, 0, -1):
        username = input("Username: ")
        password = input("Password: ")
        
        if cek_password(password):
            tampilkan_pesan_berhasil()
            break
        else:
            tampilkan_pesan_gagal(kesempatan - 1)
    else:
        tampilkan_pesan_akses_ditolak()

login()
