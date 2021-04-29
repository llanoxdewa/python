from math import pi


def count_luas_lingkaran(r):
	if type(r) not in [int,float]:
		raise TypeError("the value must be int or float")
	if r<0:
		raise ValueError("The value must be positif")
	return pi*(r**2)

if __name__=='__main__':
	print(count_luas_lingkaran(7))

