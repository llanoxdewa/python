
###################### pertukaran nilai antar variabel ################# 
## cara yang kurang pythonic
# a = 10 
# b = 20
# print("sebelum pertukaran")
# print(f'nilai a {a} \nnilai b {b}')
# c = a
# a = b
# b = c
# print('sesudah pertukaran')
# print(f'nilai a {a} nilai b {b}')
a,b,c,d = 10,20,30,40
print('sebelum pertukaran')
print((f'nilai a {a} \nnilai b {b} \nnilai c {c} \nnilai d {d}'))
print('sesudah pertukaran')
a,b,c,d = d,c,b,a
print((f'nilai a {a} \nnilai b {b} \nnilai c {c} \nnilai d {d}'))

