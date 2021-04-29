dataNama = [] 
dataUmur = []
i = 0
while(i == 0):
    nama = str(input('masukan nama anda :'))
    umur = str(input('masukan umur anda :'))
    dataNama.append(nama)
    dataUmur.append(umur)
    Q = str(input('selesai Y/N ?'))
    if Q == 'Y':
        i = 1
    
print('\n',10*'=','DATA SISWA',10*'=')

for i in range(len(dataNama)):
    print(f'\nnama siwa  : {dataNama[i]}')
    print(f'umur siswa : {dataUmur[i]}') 
    i += 1


    
