# kita harus menghitung banyak-nya pembuangan bilangan agar 
# array yang diberikan semua anggotanya sama 

contoh = [3,3,3,2,2,1,4,5,6]

# cara pribadi
def count(arr):
	jmlh_max = [arr.count(bil) for bil in set(arr)]
	return len(arr)-max(jmlh_max)

#cara dari indonesia belajar
# def count(arr):
# 	bil_unik = set(arr)
# 	jml_per_bil = [arr.count(x) for x in bil_unik]
# 	return len(arr)-max(jml_per_bil)

# cara dari indonesia belajar ke-2
# def count(arr):
# 	return len(arr)-max([arr.count(bil) for bil in set(arr)])

print(count(contoh))


