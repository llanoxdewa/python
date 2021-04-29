# angka pertama melambangkan len(array)
# baris kedua melambangkan banyaknya rotasi
# melakukan query bersasarkan 3 index

# kasus ke-1
banyaknya_rotasi = 2
inputan = [1,2,3]
index_angka_yg_dicari = [0,1,2]

def rotation_array(arr,index_num,n_R):
	n_R %= len(arr)
	arr = arr[-n_R:] + arr[:-n_R]
	return [arr[x] for x in index_num]

for y in rotation_array(inputan,index_angka_yg_dicari,banyaknya_rotasi):
	print(y)






