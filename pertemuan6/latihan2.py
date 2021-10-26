# Nama : Alian Hakim
# NIM : D11191010
# Pertemuan 6

def nilai_akhir(nilai_uas,nilai_uts,nilai_tugas):
    uas = (nilai_uas * 40) / 100
    uts = (nilai_uts * 30) / 100
    tugas = (nilai_tugas * 30) / 100
    hasil = uas + uts + tugas
    if(hasil >= 80):
        return 'A'
    elif(hasil >= 70):
        return 'B'
    elif(hasil >= 50):
        return 'C'
    elif(hasil >= 10):
        return 'D'
    else:
        return 'E'

print(nilai_akhir(50,30,100))
