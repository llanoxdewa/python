# yang akan direturn adalah posisi tikus yang paling dekat dengan tikus
# jika posisi cat relatif sama yang akan direturn adalah tikus
import math
kasus1 = [1,2,3]
kasus2 = [1,3,2]

def cat_to_mouse(kasus):
	catA = abs(kasus[2]-kasus[0])
	catB = abs(kasus[2]-kasus[1])
	if catA < catB:
		return 'Cat A'
	return 'Cat B' if catB < catA else 'mouse C'

print(cat_to_mouse(kasus1))
print(cat_to_mouse(kasus2))

