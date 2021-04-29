listku = [20,40,50,80,50,30,40,10]
print(f'listku : {listku}')
listkosong = []
print(f'\nlist kosong : {listkosong}')
# list dengan memuat lebih dari satu jenis data
apa = [12,7.3,True,'hello dude',[10,'yai']]
print(f'\nlist dengan lebih dari satu jensi data : {apa}')
# memanggil anggota pada suatu list berdasarkan index yang dimulai dari nol
#a = input('data list mana yang ingin anda ambil ?')

#if a == 'listku':
    # print(listku)
    # i = 1
    # while(i == 1):
    #     b = int(input('\nanda ingin mengambil data ke ?'))
    #     print(listku[b-1])
    #     f = str(input('keluar Y/N ?'))
    #     if f == 'Y':
    #         i = 0
#elif a == 'apa':
    # print(apa)
    # i = 1
    # while(i == 1):
    #     g = int(input('\nanda ingin mengambil data ke ?'))
    #     print(apa[g-1])
    #     g = str(input('\nkeluar Y/N ?'))
    #     if g == 'Y':
    #         i = 0

# mengubah nilai suatu list
apa[3] = 'hello bangsat'
print(f'\nlist apa yg sudah dirubah nilai : {apa}')

# penambahan data pada list/append
listku.append('data baru')
print(f'\nlistku : {listku}')

# mengeluarkan nilai list pada index paling akhir
var_tempe = listku.pop()
print(f'\nlistku yang sudah di pop : {listku}')
print(f'\nvar_tmp : {var_tempe}')

# menghapus anggota pada suatu list
listku.remove(40)
print(f'\nlistku yang sudah di remove 40 : {listku}')




