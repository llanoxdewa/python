## mencari pasangan bilangan yang jika di jumlahkan harus menghasilkan nilai yang telah ditentukan
kelipatan = 3
bilangan = [1,3,2,6,1,2]
## solusi ke-1
# def kelipatanNilai(bilangan,kelipatan):
# 	counter = 0
# 	for i in range(len(bilangan)-1):
# 		for j in range(i+1,len(bilangan)):
# 			if (bilangan[i]+bilangan[j])%kelipatan == 0:
# 				counter += 1
# 	return counter
# print(kelipatanNilai(bilangan,kelipatan))

## solusi ke-2
# def kelipatanNilai(bilangan,kelipatan):
# 	counter = 0
# 	for i,nilai1 in enumerate(bilangan[:-1]):
# 		for nilai2 in bilangan[i+1:]:
# 			if (nilai1+nilai2)%kelipatan == 0:
# 				counter += 1
# 	return counter
# print(kelipatanNilai(bilangan,kelipatan))

## for solusi ke-3
def kelipatanNilai(bilangan,kelipatan):
	counter = 0
	for i,nilai1 in enumerate(bilangan[:-1]):
		counter += len([nilai2 for nilai2 in bilangan[i+1:] if (nilai1+nilai2)%kelipatan==0]) 
	return counter
print(kelipatanNilai(bilangan,kelipatan))