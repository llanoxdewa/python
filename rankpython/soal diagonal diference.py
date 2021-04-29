import math 
matrix_3x3 = [
		[11,2,4],
		[4,5,6],
		[10,8,-12]
]
## menggunakan cara 1
# def jumlah(matriks):
# 	n = len(matriks)
# 	dig1 = sum((matriks[i][i] for i in range(n)))
# 	dig2 = sum((matriks[i][n-i-1] for i in range(n)))
# 	return f'selisih diagonal satu dan diagonal dua adalah {abs(dig1 - dig2)}'
# print(jumlah(matrix_3x3))

## menggunakan cara 2
def jumlah(arr):
	dig1,dig2 = 0,0
	n = len(arr)
	for i in range(n):
		dig1 += arr[i][i]
		dig2 += arr[i][n-i-1]
	return abs(dig1 - dig2)
print(jumlah(matrix_3x3))
