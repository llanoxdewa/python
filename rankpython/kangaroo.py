# x1 < x2 
# v1 harus > dari v2 agar dapat menyamai kecepatan dan mengerajr posisi
x1,v1,x2,v2 = 0,3,4,2

def kangoro(x1,v1,x2,v2):
	if v1 <= v2:
		return 'No'
	while x1 != x2:
		x1 += v1
		x2 += v2
	return 'Yes' if x1 == x2 else 'No'
print(kangoro(x1,v1,x2,v2))
