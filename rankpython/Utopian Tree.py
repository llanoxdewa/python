# lawra akan menanam pohon utopian
"""
jika periode genap tinggi pohon akan ditambah 1
jika periode ganjil tinggi pohon akan dikali 2
"""
periode = [i for i in range(6)]
# heigh = [1,2,3,6,7,14]
# periode_and_heigh = {per:heigh for (per,heigh) in zip(periode,heigh)}
periode_input = [0,1,4] 
# def count_tinggi_pohon(periode_and_heigh,periode_input):
# 	for per in periode_input:print(periode_and_heigh[per])

# cara ke-2 dari channel indonesia belajar
def count_tinggi_pohon(periode):
	heigh = 1
	for per in range(1,periode+1):heigh = heigh+1 if per%2==0 else heigh*2
	return heigh
for per in periode_input:print(count_tinggi_pohon(per))