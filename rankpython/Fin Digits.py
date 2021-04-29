### kita harus memecah digits

# kasus 1
# bil = 12
# # kasus 2
# bil = 1012

# def count_digits(bil):
# 	hasil = [int(b) for b in str(bil) if int(b)>0 if bil%int(b)==0]
# 	return len(hasil)

## cara ke-1 dari indonesia belajar
#def count_digits(bil):
	# jmlh = 0
	# for x in str(bil):
	# 	x = int(x)
	# 	if x==0:
	# 		continue
	# 	elif bil%x==0:
	# 		jmlh += 1
	# return jmlh

## cara ke-2 dari channel indonesia belajar
# menggabungkan ternarry ekspression dengan list comprehension
# def count_digits(bil):
# 	hb = sum([1 if bil%int(b)==0 else 0 for b in str(bil) if int(b)!=0 ])
# 	return hb

# print(count_digits(bil))











