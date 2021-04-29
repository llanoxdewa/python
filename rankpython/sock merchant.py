# mencari pasangan angka yang sama
# dimana setiap angka mewakili setiap warna dari kaos kaki

kaos_kaki = [10,20,20,10,10,30,50,10,20]

### cara pribadi 
# def hitung_pasangan_kaos_kaki(kaos_kaki):
# 	pasangan = 0
# 	for i in set(kaos_kaki):
# 		if kaos_kaki.count(i) % 2 == 0 or (kaos_kaki.count(i)-1) % 2 == 0:
# 			pasangan += (kaos_kaki.count(i) // 2)
# 	return pasangan


# solusi dari indonesia belajar (menggunakan data set dan dictionary)
# def hitung_pasangan_kaos_kaki(kaos_kaki):
# 	warna_unik = set(kaos_kaki)
# 	jml_per_warna = {warna:0 for warna in warna_unik}
# 	for warna in kaos_kaki:
# 		jml_per_warna[warna] += 1
# 	jml_pasangan = 0
# 	for warna in warna_unik:
# 		jml_pasangan += jml_per_warna[warna] // 2
# 	return jml_pasangan

# solusi ke-2 dari indonesia belajar menggunakan list komprehension
# def hitung_pasangan_kaos_kaki(kaos_kaki):
# 	warna_unik = set(kaos_kaki)
# 	jml_pasangan = 0
# 	for warna in warna_unik:
# 		jml_pasangan += len([i for i in kaos_kaki if i == warna])//2
# 	return jml_pasangan

# solusi ke-3 dari indonesia belajar paling ringkas
def hitung_pasangan_kaos_kaki(kaos_kaki):
	# tingkat kemanusiaannya rendah
	return sum([len([x for x in kaos_kaki if x == warna])//2 for warna in set(kaos_kaki)])
print(hitung_pasangan_kaos_kaki(kaos_kaki))




