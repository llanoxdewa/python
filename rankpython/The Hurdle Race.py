# kita harus menghitung jumlah magic poison yang digunakan
# magic poison akan digunakan bila kemampuan lompat tertinggi
# kurang dari tiang gawang yang harus dilompati
jump = 4
hurdle = [1,6,3,5,2]
"""
def Hurdle(jump,hurdle):
	poison = sum([1 if h > jump else 0 for h in hurdle])
	return poison
print(f'jumlah poison yang dibutuhkan : {Hurdle(jump,hurdle)}')
"""
# cara dari indonesia belajar
def Hurdle(jump,hurdle):
	dosis = max(hurdle)-jump
	return dosis if dosis > 0 else 0
print(Hurdle(jump,hurdle))




