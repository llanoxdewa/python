#### ok disini kta akan mencari tagihan 
bon = [3,10,2,9]
foodgn = 1
tagihanR = 12

## cara ke-1
# def bont(foodgn,bon,tagihanR):
# 	bonR = (sum(bon) - bon[foodgn]) // 2
# 	if bonR == tagihanR:
# 		bonR = 'bon apetit'
# 	elif bonR != tagihanR:
# 		bonR = tagihanR - bonR
# 	return bonR

## cara ke-2
def bont(foodgn,bon,tagihanR):
	bonR = (sum(bon) - bon[foodgn]) // 2
	return 'bon apetit' if bonR == tagihanR else (tagihanR - bonR)
	
print(bont(foodgn,bon,tagihanR))




