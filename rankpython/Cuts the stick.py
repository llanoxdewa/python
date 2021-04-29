# sample input = 5 4 4 2 2 8
# sample output = 6 4 2 1

panjang_kayu_awal = [1,2,3,4,3,3,2,1]

# cara pribadi
# def count_long_kayu(k):
# 	mini,hasil = min(k),[]
# 	for _ in range(len(k)):
# 		k = [bil-mini for bil in k if bil>0]
# 		if len(k)>0:hasil.append(len(k))
# 	return hasil

# cara indonesia belajar
# def count_long_kayu(k):
# 	hasil = []
# 	while k:
# 		hasil.append(len(k))
# 		cut = min(k)
# 		k = [n-cut for n in k if n!=cut]
# 	return hasil

# cara ke-2 dari channel indonesia belajar
def count_long_kayu(k):
	if k:
		cut = min(k)
		yield len(k) 
		yield from count_long_kayu([n-cut for n in k if n!=cut])

iterator = iter(count_long_kayu(panjang_kayu_awal))
for panjang in count_long_kayu(panjang_kayu_awal):
	print(panjang)





















