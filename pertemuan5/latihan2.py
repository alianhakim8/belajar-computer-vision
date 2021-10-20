# Alian Hakim
# D11191010
# pertemuan 5

nilai_celcius = int(input('Masukan nilai celcius : '))
pilih = int(input('Pilih Konversi (1-3) : '))

if(pilih == 1) :
    hasil_konversi_reamur = nilai_celcius / 1.25
    print('celcius ke reamur = ',hasil_konversi_reamur)
elif(pilih == 2):
    hasil_konversi_fahrenheit = (nilai_celcius * 9/5) + 32
    print('celcius ke fahrenheit = ',hasil_konversi_fahrenheit)
elif(pilih == 3):
    hasil_konversi_kelvin = nilai_celcius  + 273.15
    print('celcius ke kelvin = ',hasil_konversi_kelvin)
else:
    print('Pilihan tidak valid')