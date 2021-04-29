############ menggabungkan list comprehension dan fungsi map pada python #####
nama,usia = ['bejo','karti','ujang'],[23,32,18]
listku = [[d_nama,d_usia]for d_nama,d_usia in zip(nama,usia)]
def dataSiswa(x,y):
    return f'nama : {x} \nkelas : {y}'

dataSiswa = list(map(dataSiswa,nama,usia))
print(listku)
for item in dataSiswa:
    print(item)