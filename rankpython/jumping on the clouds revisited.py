

deret_awan = [0,0,1,0,0,1,1,0,0]
jarak_lompatan = 2 # k


# def count_energi(c,k):
# 	c = c*k if len(c)%k!=0 else c
# 	energi = 100
# 	for cloud in c[::k]:
# 		energi -= 1
# 		if cloud==1:energi -= 2
# 	return energi

## cara dari indonesia belajar
# def count_energi(c,k):
# 	c = c*k if len(c)%k!=0 else c
# 	awan = c[::k]
# 	return 100-len(awan)-(2*sum(awan)),awan,c


print(count_energi(deret_awan,jarak_lompatan))





























