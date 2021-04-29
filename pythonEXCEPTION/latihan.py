
try:
    print('masukan angka bilangan bulat positif')
    angka = int(input('\n>>'))
    if angka < 0:
        raise ValueError('input harus bilangan bulat positif') 
    else:
        print(angka)   
except ValueError as e:
    while(angka < 0):
        print(e)
        angka = int(input('\n>>'))
    else:
        print(angka)
    




