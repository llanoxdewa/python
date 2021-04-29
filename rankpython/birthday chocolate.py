# setiap cokelat harus dipotong sebanyak bulan lahir ron dan hasil jumlah dari dua bilangan yang dipotong harus bernilai tanggal ron

chocolate = [1,2,1,3,2]
ronD,ronM,notasi = 3,2,0
# def countCokelat(chocolate,notasi,ronD,ronM):
# 	for i in range(len(chocolate)-1 if len(chocolate)>1 else len(chocolate)): #atau bisa menggunakan for i in range(len(chocolate)-m+1):
# 		if sum(chocolate[i:i+ronM]) == ronD:
# 			notasi += 1
# 	return f'banyaknya cokelat adalah : {notasi}'

# print(countCokelat(chocolate,notasi,ronD,ronM))
## solusi ke-2
# def cokelat(c,d,m):
# 	notasi = 0
# 	for i in range(len(c)-m+1):
# 		notasi += 1 if sum(c[i:i+m]) == d else 0
# 	return notasi
# print(cokelat(chocolate,ronD,ronM))

## solusi ke-3 menggunakan list komprehension
cokelat = [ 1 if sum(chocolate[i:i+ronM])==ronD else 0 for i in range(len(chocolate)-ronM+1)]
print(sum(cokelat))