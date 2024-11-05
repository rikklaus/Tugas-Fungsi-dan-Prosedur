# Nama: Erik Klaus Keifas Kalalo
# Kelas: 1A
# NIM: 2400887

def konversi_waktu(total_waktu):
        jam = total_waktu // 3600
        sisa = total_waktu % 3600
        menit = sisa // 60
        detik = sisa % 60
        return jam, menit, detik

def hitungwaktu ():
        print("Input waktu mulai:    ")
        jam_mulai = int(input("Jam:     "))
        menit_mulai = int(input("Menit:     "))
        detik_mulai = int(input("detik:     "))
        
        print("Input waktu selesai:    ")
        jam_selesai = int(input("Jam:     "))
        menit_selesai = int(input("Menit:     "))
        detik_selesai = int(input("Detik:     "))
        
        total_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
        total_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
        total_waktu = total_selesai - total_mulai
        
        hasiljam, hasilmenit, hasildetik = konversi_waktu(total_waktu)
        print(f"{hasiljam} Jam - {hasilmenit} Menit - {hasildetik} Detik")
        
hitungwaktu()