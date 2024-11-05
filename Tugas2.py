# Nama: Erik Klaus Keifas Kalalo
# Kelas: 1A
# NIM: 2400887

def login ():
    print("Silakan Login")
    
    for kesempatan in range (3,0,-1):
        username = (str(input("Username:    ")))
        password = (str(input("Password:    ")))
        if password == "latihan":
            print("Selamat datang di aplikasi Dasar Pemrograman")
            break
        else:
            print(f"Login salah! kesempatan anda {kesempatan - 1} kali lagi")
    
    else:
        print("Anda tidak diperkenankan mengakses aplikasi ini")
    
login()