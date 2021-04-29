number = [1,2,3,4,5]

## cara pribadi
# def count(arr):
# 	n,dataN = len(arr),[]
# 	for i in range(n):
# 		dataN.append(sum(arr)-arr[i])
# 	return f'selisihnya adalah : {max(dataN)-min(dataN)}\nmax dataN : {max(dataN)}\nmin dataN : {min(dataN)}'
# print(count(number))



## cara indonesia belajar
# def minmaxsum(arr):
# 	mini,maxi = arr[0],arr[0]
# 	for i in arr:
# 		if i < mini:
# 			mini = i
# 		if i > maxi:
# 			maxi = i
# 	print(f'nilai dari mini : {mini}\nnilai dari maxi : {maxi}\nnilai dari summax : {sum(arr)-maxi}\nnilai dari summin : {sum(arr)-mini}')
# minmaxsum(number)


## cara yang amazing simpel
# def hitung(arr):
# 	return f'maxsum : {sum(arr)-max(arr)}\nminsum : {sum(arr)-min(arr)}'
# print(hitung(number))

## cara ke 2 dari indonesia belajar
# def hitung(arr):
# 	arr.sort()
# 	print(sum(arr[:-1]),'\n',sum(arr[1:]))
# hitung(number)


## cara ke 3 dari indonesia belajar
def hitung(arr):
	terurut = sorted(arr)
	print(sum(terurut[:-1]),sum(terurut[1:]))
hitung(number)
