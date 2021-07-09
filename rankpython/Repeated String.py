# harus mengulang string kata sebanyak n kali

kata = 'aba'
n = 10

# cara pribadi 
# def count_huruf(kata,n):
# 	selisih = (n//len(kata))
# 	kata_tambahan = n-(len(kata)*selisih)
# 	if len(kata)%n==0:
# 		kata *= selisih
# 		return kata.count('a')
# 	else:
# 		kata *= selisih
# 		kata += kata[:kata_tambahan]
# 		return kata.count('a')

# cara dari indonesia belajar
 def count_huruf(kata,n):
 	pos = [n for n,x in enumerate(kata) if x == 'a']
 	res = len(pos) * (n//len(kata))
 	sisa = n%len(kata)
 	res += len([x for x in pos if x<sisa])
 	return res
print(count_huruf(kata,n))

















