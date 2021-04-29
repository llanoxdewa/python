# (*)args adalah sebuah argumen pada suatu fungsi yang mengembalikan 
# objek iterabel berupa sebuah tuple
# def penjumlahan(*angka):
# 	return sum(angka)
# print(penjumlahan(1,2,3,4,5,6,7,8))


# kwargs adalah sebuah argumen yang akan mengembalika dicktionary
# contoh def fugnsi(key='value')
# def cek_nilai(**data):
# 	for nama in data:
# 		print(f'{nama} mendapat nilai {data[nama]}')
# 	print(data)
# cek_nilai(llano=100,ujang=200,taro=120,kimak=60)


## menggabungkan *args dan **kwargs 
# def fungsi(*args,**kwargs):
# 	print(args)
# 	print(kwargs)

# fungsi(10,'llano','kuda',101011,'tayo',
# 		nama='llano',kelas=11)