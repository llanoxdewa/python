import math

sampel = [4,6,5,3,3,1]
# sampel output

# cara mandiri men
# def cara(sampel):
# 	for bil in sampel:
# 		if abs(bil-min(sampel))>1:
# 			sampel.remove(bil)
# 	return sampel


# print(cara(sampel))

# cara indonesia belajar
def picking_number(arr):
    unik = sorted(set(arr))
    n_max = max([arr.count(bil) for bil in unik])
    for x,y in zip(unik,unik[1:]):
        if abs(x-y) not in (0,1):
            continue
        else:
            n = arr.count(x) + arr.count(y)
            n_max = max(n_max,n)
    return n_max

print(picking_number(sampel))










