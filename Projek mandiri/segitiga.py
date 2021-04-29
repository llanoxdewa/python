# segitiga siku siku
for x in range(1,11):
	print('*'*x)

print('\n')

# segitiga siku siku terbalik 90
for _ in range(1,11):
	n = 10
	print('*'*n)
	n -= 1

# segitiga siku siku terbalik
for i in range(1,11):
	print(' '*(10-i)+'*'*i)

print('\n')

# segitiga sama kaki
for i in range(1,11):
	print(' '*(10-i)+'* '*i)

print('\n')

# segitiga sama kaki terbalik
for x in range(1,11):
	print('*'*x if x <= 5 else '*'*(10-x))

print('\n')

#segitiga diamond 
for x in range(1,11):
	print(' '*(10-x)+'* '*x if x <= 5 else ' '*(x)+'* '*(10-x))

print('\n')

# segitiga 































# class Gambar_segitiga:

# 	def __init__(self,panjang_alas):
# 		self.panjang_alas = panjang_alas

# 	def Segitiga_diamond(self):
# 		n = self.panjang_alas
# 		for x in range(1,n):
# 			print(' '*(n-x)+'* '*x if x <= (n//2) else ' '*(x)+'* '*(n-x))

# 	def segitiga_siku_siku(self):
# 		n = self.panjang_alas
# 		for x in range(1,n):
# 			print('*'*x)

# 	def segitiga_sama_kaki(self):
# 		n = self.panjang_alas
# 		for x in range(1,n):
# 			print(' '*(n-x)+'* '*x)

# 	def segitiga_siku_siku_terbalik(n):
# 		n = self.panjang_alas
# 		for _ in range(1,n+1):
# 			print('*'*n,n)
# 			n -= 1 if n>1 else 0

# panjang_alas = int(input('masukan panjang alas >> '))
# jenis_segitiga = input('masukan jenis segitiga >> ')
# segitiga = Gambar_segitiga(panjang_alas)

# if jenis_segitiga == 'siku siku':
# 	segitiga.segitiga_siku_siku()
# elif jenis_segitiga == 'sama kaki':
# 	segitiga.segitiga_sama_kaki()
# elif jenis_segitiga == 'siku siku terbalik':
# 	segitiga.segitiga_siku_siku_terbalik()
# elif jenis_segitiga == 'diamond':
# 	segitiga.Segitiga_diamond()





