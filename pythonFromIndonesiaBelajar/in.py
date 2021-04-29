# listku = [i for i in range(10,60,10)]
# cari = int(input('masukan angka >> '))
# ketemu = 'angka ditemukan' if cari in listku else 'angka tidak ditemukan'
# print(f'hasil nya : {ketemu}')
nama = str(input('>> '))
## cara tidak pythonic
# if nama  == 'bejo' or nama == 'tejo' or nama == 'karti':
# 	print('siswa teladan')
# else:
# 	print('siswa regular')
if nama in ('llano','bejo','kartini'):
	print('siswa teladan')
else:
	print('siswa bandel')