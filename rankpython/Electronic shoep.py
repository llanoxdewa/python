# elektronic shop 
# 10(batasan harga) 2(jumlah pilihan keyboard) 3(jumlah pilihan usb driver)
# 3 1
# 3 2 8

keyboard,usb,limit = [4],[5],5

# cara dari olah pikir pribadi
# def H_shop(limit,keyboard,usb):
# 	try:
# 		jumlah = max([max([u+k for u in usb if u+k <= limit])for k in keyboard])
# 	except:
# 		return -1
# 	return jumlah 

# cara ke-1 dari channel indonesia belajar
# def H_shop(limit,keyboard,usb):
# 	spending = sorted([k+u for k in keyboard for u in usb])
# 	for harga in spending[::-1]:
# 		if limit-harga >= 0:
# 			return harga
# 	return -1

# cara ke-2 dari channel indonesia belajar
def H_shop(limit,keyboard,usb):
	spending = [k+u for k in keyboard for u in usb]
	spending.append(-1)
	return max([harga for harga in spending if harga < limit])

print(H_shop(limit,keyboard,usb))