"""
untuk referensi lebih lengakap bisa dilihat di e_book python hal 130

"""


nama = 'llano kusuma dewa'
bil = '1'
print(bil.isdecimal())

# # list slicing pada string
# print(nama[::-1])
# print(nama[:6])

# # memeriksa apakah suatu kata terdapat dalam suatu string
# print('yes' if 'llano' in nama else 'No')

# # mengubah seluruh isi varibel string menjadi upper case
# print(nama.upper())
# # mengubah seluruh isi varibel string menjadi lower case
# print(nama.lower())
# # memeriksa suatu variabel string apakah upper case atau lowercase/uppercase
# print(nama.islower())
# print(nama.isupper())

# the isX string methods 
## memeriksa apakah variabel sting hanya mengandung huruf dan tidak kosong
# print(nama.isalpha())
## memeriksa apakah variabel sting hanya mengandung huruf dan angka dan tidak kosong
# print(nama.isalnum())
## memeriksa apakah variabel sting hanya mengandung angka dan tidak kosong
# print(nama.isdecimal())
# # memeriksa apakah variabel sting hanya mengandung spasi,tab,new line dan tidak kosong
# print(nama.isspace())
## memeriksa apakah variabel sting hanya mengandung huruf kapital atau uppercase lalu diikuti oleh lowercase dan tidak kosong
# print(nama.istitle())

## endwith and startwith method
# memeriksa apakah suatu string diawali dan diakhiri dengan kata \ huruf sesaui parameter yang diberikan
# print(nama.startswith('llano'))
# print(nama.endswith('dewa'))

## ljust,rjust,center method
# print(nama.rjust(20))
# print(nama.ljust(20))
# print(nama.center(20,'-'))

# contoh program
# def printPicnic(itemsDict, leftWidth, rightWidth):
# 	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
# 	for k, v in itemsDict.items():
# 		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)


## contoh program isx method
# user_name = ''
# password = ''

# while True:
# 	user_name = input('your user name (only contain character) ')
# 	if user_name.isalpha():
# 		print('great your username is valid')
# 		break
# 	print('user name is not valid')

# while True:
# 	password = input('your password (only contain character and number) ')
# 	if password.isalnum():
# 		print('your password is valid')
# 		break
# 	print('your password is not valid')

# print('your user name is ',user_name)	
# print('your password is ',password)

















