# Alian Hakim
# D11191010
# Pertemuan 6

min = int(input('Masukan bilangan awal : '))
max = int(input('Masukan bilangan akhir : '))
pilihan = input('tampilkan ganjil/genap ? : ')

for i in range(min, max):
    if(pilihan == 'ganjil'):
        if(i % 2 != 0):
            print(i)
    elif(pilihan == 'genap'):
        if(i % 2 == 0):
            print(i)
    else:
        print('pilihan tidak valid')
