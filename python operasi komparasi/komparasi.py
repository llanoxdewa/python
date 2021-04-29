# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 2
b = 4 

# lebih besar dari
print("=========lebih besar dari=======")
hasil = a > 3
print( a,'>',3 ,'=',hasil)
hasil = b > 3
print( b,'>',3 ,'=',hasil)


# kurang dari 
print("========kurang dari===========")
hasil = a < 3
print( a,'<',3 ,'=',hasil)
hasil = b < 3
print( b,'<',3 ,'=',hasil)

# lebih dari sama dengan 
print("========lebih dari sama dengan===========")
hasil = a >= 3
print( a,'>=',3 ,'=',hasil)
hasil = b >= 4
print( b,'>=',4 ,'=',hasil)

# lebih dari sama dengan 
print("========kurang dari sama dengan===========")
hasil = a <= 3
print( a,'<=',3 ,'=',hasil)
hasil = b <= 4
print( b,'<=',4 ,'=',hasil)

# sama dengan
print("=========sama dengan===========")
hasil = a == a
print(a, '==', a, '=',hasil)
hasil = a == b 
print(a, '==', b, '=',hasil)

# tidak sama dengan
print("=========tidak sama dengan===========")
hasil = a != a
print(a, '!=', a, '=',hasil)
hasil = a != b 
print(a, '!=', b, '=',hasil)

# 'is' sebagai komparasi objek identity
print("====is=====")
x = 5 # ini adalah assigment membuay objek 
y = 5
print('nilai x =', x, 'id = ', hex(id(x)))
print('nilai y =',y, 'id = ', hex(id(y)))
hasil = x is y 
print("x is y =",hasil)

# 'is not' sebagai komparasi objek identity
print("====is not=====")
x = 5 # ini adalah assigment membuay objek 
y = 6
print('nilai x =', x, 'id = ', hex(id(x)))
print('nilai y =',y, 'id = ', hex(id(y)))
hasil = x is not y 
print("x is not y =",hasil)


