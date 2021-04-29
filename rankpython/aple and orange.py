s,t,a,b = 7,11,5,15
aple,orange = [-2,2,1],[5,-6]

def countApleAndOrange(s,t,a,b,apples,oranges):
	# jmlhApel,jmlhJeruk = 0,0
	# apl = [a+d for d in aple]
	# jrk = [b+d for d in orange]
	# for d in apl:
	# 	if d in range(s,t+1):
	# 		jmlhApel += 1
	# for d in jrk:
	# 	if d in range(s,t+1):
	# 		jmlhJeruk += 1
	# print(f'jmlh aple : {jmlhApel}')
	# print(f'jmlh jeruk : {jmlhJeruk}')
	apl = [1 if a+d in range(s,t+1) else 0 for d in apples]
	jrk = [1 if b+d in range(s,t+1) else 0 for d in oranges]
	print(sum(apl))
	print(sum(jrk))
countApleAndOrange(s,t,a,b,aple,orange)



	