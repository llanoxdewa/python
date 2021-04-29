# mencari like

# contoh input = 3 >> jumlah like pada iklan pada hari ke-3

banyak_pengiklan = [i for i in range(1,6)]
banyak_hari = 3

# cara pribadi
# def count_like(banyak_pengiklan,banyak_hari):
# 	banyak_like = 0
# 	banyak = len(banyak_pengiklan)
# 	for hari in range(banyak_hari):
# 		banyak = (banyak//2) if hari == 0 else (banyak*3)//2
# 		banyak_like += banyak
# 	return banyak_like

## cara dari indonesia belajar

# cara ke-1
def count_like(banyak_pengiklan,banyak_hari):
	like_ctr = [2] # [2,3,4]
	for _ in range(banyak_hari-1):
		like_ctr.append(like_ctr[-1]*3//2)
	return sum(like_ctr)d


print(count_like(banyak_pengiklan,banyak_hari))















