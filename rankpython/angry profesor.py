# profesor yang marah 
# 'yes' jika siswa yang hadir < minimum yang telah ditentukan else 'no'
# kasus 1 
# min_tepat_waktu = 3
# data_waktu_hadir_siswa = [-1,-3,4,2]

#kasus 2
min_tepat_waktu = 2
data_waktu_hadir_siswa = [0,-1,2,1]

def count_siswa_biadab(minimum,data):
	return 'Yes' if (sum([siswa for siswa in data if siswa <= 0]) < minimum) else 'No'

print(count_siswa_biadab(min_tepat_waktu,data_waktu_hadir_siswa))















