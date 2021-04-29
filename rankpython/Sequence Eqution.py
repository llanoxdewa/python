

# p1 = 2
# p2 = 3
# p3 = 1
# dengan rumus sampel[x],sampel[sampel[y]]
# x = 1 = sampel[3] maka sampel[sampel[3]] maka akan mereturn 2 karena sampel[3] = sampel[2]

# def count_permutasion(p):
# 	x = [x for x in range(1,len(p)+1)]
# 	y = [(p.index(p.index(bil)+1)+1) for bil in x if bil in p]
# 	#for bil in x:y.append(p.index(p.index(bil)+1)+1)
# 	return y

# sampel = [4,3,5,1,2]
# #cara dari indonesiabelajar
# def count_permutasion(p):
# 	n = len(p)
# 	peta = {v:i+1 for i,v in enumerate(p)}
# 	return [peta[peta[i]] for i in range(1,n+1)]

# # for v in count_permutasion(sampel):print(v)
# peta = {v:i+1 for i,v in enumerate(sampel)}
# print(count_permutasion(sampel))
# print(peta)
























