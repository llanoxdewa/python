# python built in class
# bool : nilai boolean
# int : bilangan bulat
# float : bilangan berkoma
# list : kumpulan objek
# tuple : kumpulan objek
# str : Character string
# set : kumpulan objek yang berbeda (tidak berurut)
# frozenset : kumpulan objek dan tidak bisa memaut elemen yang sama 
# dict : mapping(dictionary)

######### List ###########
l = list("LLANO")

for i in range(len(l)):
    print(l[i])
print(l)

########## TUPLE #######
l = (1,2,3)
print(l)

###### set / frozenset #######33
x = frozenset("hello world")
l = {1,2,3,}
z = {(1,2,3),(1,1,2,3),x}
print(l)
print(f'frozen set {z}')

####### DICTIONARY #######
D1 = [('nama','llano'),('umur',16)]
D = dict(D1)
print(D)

######### SESUATU YANG KEREN ##########
data = [1,2,3,4,5,6,7]
for angka in data:
    print('\n',angka)