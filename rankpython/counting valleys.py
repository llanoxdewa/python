### mencatat perjalanan gary
# naik : U
# turun : D
# mencari banyak lembah yang dilalui
# 1 lembah terdiri dari 3D dan 3U
track = ['U','D','D','D','U','D','U','U']

# cara ke-1 dari channel indonesia belajar (menggunakan dictionary)
# def H_lembah(track):
# 	valley_count=sea_level=1
# 	cases = {'U':1,'D':-1}
# 	for x in track:
# 		if sea_level > 0:
# 			sea_level += cases[x]
# 			continue
# 		sea_level += cases[x] # akan tibambah dengan 1 jika U dan -1 jika D
# 		if sea_level == 0:
# 			valley_count += 1
# 	return valley_count

# cara ke-2 menggunakan ternarry expression 
def H_lembah(track):
	cases = {'U':1,'D':-1}
	sea_level=valley_count=0
	for x in track:
		sea_level += cases[x]
		valley_count += 1 if x=='U' and sea_level==0 else 0
	return valley_count
print(H_lembah(track))






