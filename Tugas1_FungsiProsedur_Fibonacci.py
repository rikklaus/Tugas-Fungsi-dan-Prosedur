# Nama: Erik Klaus Keifas Kalalo
# Kelas: 1A
# NIM: 2400887

def fibonacci (n):
    a = 0
    b = 1
    
    if n == 1:
        print (a)
    else:
        print (a)
        print (b)
    
    for p in range (2,n):
        c = a+b
        a = b
        b = c
        print(c)

i = int(input("Masukkan angka: "))
print(fibonacci(i))