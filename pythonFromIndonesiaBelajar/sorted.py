import random 
def costum_key(nama):
	return nama.split()[-1]
siswa = ['llano 4','ujang 2','boedi 1','jajang 3']
print(f'sebelum di urutkan : {siswa}')
terurut = sorted(siswa, key=costum_key)
print(f'sesudah diurutkan : {terurut}')