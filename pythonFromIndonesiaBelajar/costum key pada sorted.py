# def costum_key(nama):
# 	return nama.split()[-1]
# siswa = ['karti susanti','tejo purnawan','bejo rahmadi']
# print(f'sebelum urut : {siswa}')
# terurut = sorted(siswa,key = lambda x:x.split()[-1])
# print(f'terurut : {terurut}')
listNama = []
while True:
	listNama.append(str(input('masukan nama anda >> '))+' '+str(input('masukan No absen >> ')))
	if input('quit >> ') == 'yes':
		break
print(f'list nama siswa sebelum diurutkan : {listNama}')
namaUrut = sorted(listNama,key = lambda x:x.split()[-1])
print(f'list nama siswa sesudah diurutkan {namaUrut}')
