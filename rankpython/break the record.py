# output yang diharapkan adalah jumlah perubahan nilai max dan min nya

resultGame = [10,5,20,20,4,5,2,25,1]
## solusi pertama dungs
# def breakthecode(score):
# 	low,high = score[0],score[0]
# 	n_low,n_high = 0,0
# 	for bil in score[1:]:
# 		if bil<low:
# 			low = bil
# 			n_low += 1
# 		elif bil > high:
# 			high = bil
# 			n_high += 1
# 	return f'banyaknya perubahan pada low {n_low} dan high {n_high}'
# print(breakthecode(resultGame))

## solusi kedua
# def breaktherecord(score):
# 	low,high = score[0],score[0]
# 	n_low,n_high = 0,0
# 	for bil in score[1:]:
# 		low,n_low = (bil,n_low+1) if bil < low else (low,n_low)
# 		high,n_high = (bil,n_high+1) if bil > high else (high,n_high)
# 	return f'banyaknya perubahan low {n_low} dengan high {n_high}'
# print(breaktherecord(resultGame))

