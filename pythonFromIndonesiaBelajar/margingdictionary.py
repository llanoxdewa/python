data1 = {
	'nama':'llano',
	'jurusan':'elektro'
}
data2 = {
	'eskul':'IT',
	'hobi':'menjelajah internet'
}
data3 = {
	'alamat':'PERUM GRIYA JAYA CIKEAS BLOK D1 No.4',
	'nilai':100
}

siswa = {**data1,**data2,**data3}
# for key in data1:
# 	siswa[key] = data1[key]
# for key in data2:
# 	siswa[key] = data2[key]
print('nama siswa : {nama}\njurusan : {jurusan}\neskul : {eskul}\nhobi : {hobi}\nalamat rumah : {alamat}\nnilai : {nilai}'.format(**siswa))