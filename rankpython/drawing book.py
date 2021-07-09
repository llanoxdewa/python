### mencari cara tercepat untuk mengakses suatu halaman pada sebuah buku
import math
book = [[0,1],[2,3],[4,5]]
tujuanHalaman = 4
## cara pribadi 
# def hitungHalaman(book,tujuanHalaman):
# 	jumlahHd = jumlahHb = 0
# 	for i in range(len(book)):
# 		if book[i][0] == tujuanHalaman or book[i][1] == tujuanHalaman:
# 			break
# 		jumlahHd += 1
# 	for i in range(1,len(book)+1):
# 		if book[i*-1][0] == tujuanHalaman or book[i*-1][1] == tujuanHalaman:
# 			break
# 		jumlahHb += 1

# 	return jumlahHd if jumlahHd < jumlahHb else jumlahHb

# cara ke-2 dari chanel indonesia belajar
 def hitungHalaman(book,tujuanHalaman):
 	n = len(book)
 	front = tujuanHalaman // 2
 	back = abs((n-tujuanHalaman))//2
 	if tujuanHalaman % 2 != 0 and n-tujuanHalaman == 1:
 		back += 1
 	if back < front:
 		return back
 	return front

## cara ke-3 menggunakan ternarry expression
#def hitungHalaman(book,tujuanHalaman):
#	n = len(book)
#	front = tujuanHalaman//2
#	back = abs((n-tujuanHalaman))//2 + (1 if tujuanHalaman%2!=0 and n-tujuanHalaman==1 else 0)
#	return back if back < front else front
#print(hitungHalaman(book,tujuanHalaman))




















