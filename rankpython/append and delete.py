import re
# kasus 1
kata1 = 'amp'
kata2 = 'amp'
syarat = 9

def append_and_delete(kata1,kata2,syarat):
	perubahan,stop = 0,0
	for x,y in zip(kata1,kata2):
		if x != y:
			break
		stop += 1
	hapus = len(kata1) - stop #6
	tambah = len(kata2) - (len(kata1)-hapus) #4
	if tambah==0 and hapus<=syarat:
		return 'yes'
	elif hapus==0 and (hapus-tambah)%2!=0:
		return 'No'
	operasi = (hapus+tambah)
	return 'yes' if operasi<=syarat else 'No'


print(append_and_delete(kata1,kata2,syarat))










