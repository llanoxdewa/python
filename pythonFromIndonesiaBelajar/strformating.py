###################### 	FORMAT STRING PADA PYTHON ################

nama = 'bejo'
usia = 25
## CARA KURANG PYTHONIC
# print('nama saya ' + nama + ' usia saya ' + str(usia))
# print('nama saya %s usia saya %d tahun' %(nama,usia))
## CARA YANG PYTHONIC
# print('nama saya {1} usia saya {0} tahun'.format(usia,nama))
# siswa = {
# 	'nilai':100,
# 	'nama':'llano',
# 	'usia':35,
# 	'jurusan':'elektro'
# }
# print('nama : {nama}\nusia : {usia}\njurusan : {jurusan}\nnilai : {nilai}'.format(**siswa))
# print(f'nama saya : {nama} usia saya {usia}')
