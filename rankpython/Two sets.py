####### yoi #####
a = [2,4]
b = [16,32,96]
def getTotal(a,b):
	c = []
	for bil in range(a[-1],b[0]+1):
		for x in (a+b):
			if x < bil and bil % x != 0:
				break
			elif x > bil and x % bil != 0:
				break
		else:
			c.append(bil)
	return c
print(f'banyaknya bilangan yang memenuhi syarat : {len(getTotal(a,b))} \ndengan anggota : {getTotal(a,b)}')