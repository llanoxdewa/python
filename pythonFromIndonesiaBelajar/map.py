# def lipat_ganda(x,y,z):
    # return (x * y * z) // 2
# nilai_x = [1,2,3]
# nilai_y = [4,5,6]
# nilai_z = [7,8,9]
# listlipatdua = list(map(lipat_ganda,nilai_x,nilai_y,nilai_z))
#print(f'list normal : }')
# print(f'setelah di kali dua : {listlipatdua}')

def data_siswa(nama,kelas,jurusan):
    return f'\nnama siswa : {nama} \nkelas      : {kelas} \njurusan    : {jurusan}'
    
Lnama,Lkelas,Ljurusan = [],[],[]
while True:
    Lnama.append(str(input ('masukan nama >>> ')))
    Lkelas.append(int(input('masukan kelas >>> ')))
    Ljurusan.append(str(input('masukan jurusan >>> ')))
    if input('selesai ? >> ') == 'ok':
        break

# strukturnya adalah map(fungsi(),argumen1,argumen2)
dbase = tuple(map(data_siswa,Lnama,Lkelas,Ljurusan))
for item in dbase:
    print(item)



### program kirim barang::::
### membuat fungsi analisa nilai

# def analys(nama,berat,kodeBarang,tujuan):
# 	kode = {
# 		'A':'Alat elektronik',
# 		'B':'Alat nonElektronik',
# 		'C':'Alat yang mengandung bahan berbahaya',
# 		'D':'Alat berbahaya'
# 	}
# 	exberat = 'berat barang diatas 20 kg'
# 	return f'\nnama : {nama}\nberat : {berat if berat < 20 else exberat} kg\ndengan jenis barang : {kode[kodeBarang]}\ndengan tujuan : {tujuan}'
# nama,berat,kodeBarang,tujuan = [],[],[],[]
# while True:
# 	nama.append(str(input('masukan nama anda >> ')))
# 	berat.append(int(input('masukan berat barang >> ')))
# 	kodeBarang.append(str(input('masukan kode barang >> ')))
# 	tujuan.append(str(input('masukan tujuan >> ')))
# 	if input('selesai >> ') == 'yes':
# 		break

# dataH = tuple(map(analys,nama,berat,kodeBarang,tujuan))
# for data in dataH:
# 	print(data)