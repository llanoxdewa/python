# def cetak_nama(f_nama,L_nama):
# 	print(f'{f_nama} {L_nama}')

# cetak_nama('llano','dewa')
# cetak_nama(L_nama='dewa',f_nama='llano')
def cetak_data_diri(nama,kelas,jurusan):
	return f'nama : {nama}\nkelas : {kelas} \njurusan : {jurusan}'
print(cetak_data_diri(jurusan=input('masukan jurusan >> '),nama=input('masukan nama >> '),kelas=input('masukan kelas >> ')))
 