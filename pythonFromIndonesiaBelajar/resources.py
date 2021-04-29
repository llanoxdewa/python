# with open('pesan.txt','w') as fileku:
# 	fileku.write('hello llano kusuma dewa')
# 	fileku.write('\nbelajar python dengan sublime text')
# 	fileku.write('\nbelajar python bersama chanell indonesia belajar')
# 	fileku.write('\nskuy living')
# 	for i in range(1,11):
# 		fileku.write(f'\n{i}')
nama,nilai,jurusan = [],[],[]
while True:
	nama.append(str(input('masukan nama anda >> ')))
	nilai.append(str(input('masukan nilai anda >> ')))
	jurusan.append(str(input('masukan jurusan anda >> ')))
	if input('selesai ? >> ') == 'yes':
		break
with open('llano.txt','w') as file:
	file.write('DATA SISWA'.center(60,'='))
	for nama,nilai,jurusan in zip(nama,nilai,jurusan):
		file.write(f'\nnama	 : {nama}\nnilai    : {nilai}\njurusan  : {jurusan}\n')


###################### PROGRAM PATEN KALI ##############################

# nama,jurusan,eskul = [],[],[]
# while True:
# 	nama.append(str(input('masukan nama anda >> ')))
# 	jurusan.append(str(input('masukan jurusan anda >> ')))
# 	eskul.append(str(input('masukan minat dan bakat >> ')))
# 	if input('out >> ') == 'yes':
# 		break

# with open('tayo.txt','w') as data:
# 	data.write(" DATA SISWA ".center(50,'='))
# 	for namal,jurusanl,eskull in zip(nama,jurusan,eskul):
# 		data.write(f'\nnama : {namal}\njurusan : {jurusanl}\neskul : {eskull}\n')

# with open('tayo.txt','r') as data:
# 	if input('apakah anda ingin melihat data siswa >> ') == 'sure':
# 		dataB = data.read()
# 		print(dataB)
# 	
