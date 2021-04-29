lilin = [3,2,1,3]

## solusi yang sendiri / mandiri
#print(f'lilin yang dapat ditiup {lilin.count(max(lilin))}')

## solusi dari indonesia belajar
# def hitung(arr):
# 	total = 0
# 	tertinggi = max(arr)
# 	for lilin in arr:
# 		if lilin == tertinggi:
# 			total += 1
# 	print(total)
# hitung(lilin)

## solusi dengan memanfaatkan list comprehension
# def hitung(arr):
# 	lilinmax = [i for i in arr if i == max(arr)]
# 	print(len(lilinmax))
# hitung(lilin)

