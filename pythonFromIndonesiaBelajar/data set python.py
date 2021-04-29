########### data set ##########
"""
data jenis set tidak bisa menyimpan list,dictionary,dan set itu sendiri
nilai pada date set juga tidak memiliki index
"""
myset = {1,1,1,1,2,3,2,2,2,1,2,4,3,2}
print(myset)

# mengurutkan data set 
# myset_terurut = sorted(myset)
# print(myset_terurut)

# # menambahkan anggota pada data set
# # - dengan add()
# myset.add(5)
# # dengan update() update bisa lebih dari satu argumen untuk ditambah
# myset.update([6,7,8,9,1])

# menghapus nilai pada data jenis set
# fungsi discard()
# myset.discard(3)
# print(myset)
# # fungsi remove() akan menampilkan error jika anggota yg ingin dihapus kosong atau tidak ada di set
# myset.remove(3)

# operasi gabungan pada set
# data1 = {1,2,3,4}
# data2 = {1,2,7,8}
# # menggunakan tanda palang |
# print(data1|data2)
# # menggunakan fungsi union
# data3 = data1.union(data2)
# print (data3)

# operasi irisan 
# data1 = {1,2,3,4}
# data2 = {1,2,7,8}
# # menggunakan tanda palang |
# print(data1 & data2)
# # menggunakan fungsi intersection
# data3 = data1.intersection(data2)
# print (data3)

# operasi selisih 
# data1 = {1,2,3,4}
# data2 = {1,2,7,8}
# # menggunakan tanda min -
# print(data1 - data2)
# # menggunakan fungsi difference
# data3 = data1.difference(data2)
# print (data3)

# operasi komplemen
# data1 = {1,2,3,4}
# data2 = {1,2,7,8}
# # menggunakan tanda ^ 
# print(data1 ^ data2)
# # menggunakan fungsi difference
# data3 = data1.symmetric_difference(data2)
# print (data3)












