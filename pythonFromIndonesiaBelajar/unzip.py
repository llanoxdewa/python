siswa = [('llano','11 elektro 1',90),
		 ('boedi','11 elektro 2',77),
		 ('ujang','11 las 1',100)
		]
nama,kelas,nilai = zip(*siswa)
for nama,kelas,nilai in zip(nama,kelas,nilai):
	print(f'nama  : {nama}\nkelas : {kelas}\nnilai : {nilai}')