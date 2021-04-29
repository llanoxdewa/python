sampel = [-4,3,-9,0,4,1]
# def mamamia(arr):
# 	n = len(arr)
# 	bil0 = len([i for i in arr if i == 0])/n
# 	bilp = len([i for i in arr if i > 0])/n
# 	biln = len([i for i in arr if i < 0])/n
# 	print('{:07.6f}\n{:07.6f}\n{:07.6f}'.format(bilp,biln,bil0))
# mamamia(sampel)

## cara alternatif dari indoonesia belajar
# def plusMinus(arr):
# 	n = len(arr)
# 	positif,negatif,nol = 0,0,0
# 	for bil in arr:
# 		if bil == 0:
# 			nol += 1
# 		elif bil < 0:
# 			negatif += 1
# 		else:
# 			positif += 1
# 	return '{:07.6f}\n{:07.6f}\n{:07.6f}'.format(positif/n,negatif/n,nol/n)
# print(plusMinus(sampel))

## cara alternatif dari Indonesia belajar dengan fungsi filter dan lambda
def lamda(arr):
	n = len(arr)
	positif = len(tuple(filter(lambda x:x>0,arr)))/n
	negatif = len(tuple(filter(lambda x:x<0,arr)))/n
	nol = len(tuple(filter(lambda x:x==0,arr)))/n
	print("{:07.6f}".format(positif))
	print("{:07.6f}".format(negatif))
	print("{:07.6f}".format(nol))
	
lamda(sampel)


