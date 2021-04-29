
#>>> definition of decorator 
# decorator is fungsi yang mengambil fungsi lain sebagai argumennya 
# dan mengembalikan fungsi lainya sebagai sebuah nilai

# def another_function():
# 	print('another function')
# def turn_into_another_function(func):
# 	return another_function
# @turn_into_another_function
# def a_function():
# 	print('a function')
# a_function()

"""
# def mapper(func):

fungsi inner akan mengambil argumen yang diberikan pada fungsi yang menggunakan
decorator mapper dan fungsi mapper sendiri akan mengambil argumen berupa fungsi 
yang menggunakan decorator mapper

# 	def inner(lists):
# 		hello this is inner() function 
# 		return [func(name) for name in lists]

# 	return inner

# @mapper
# def camelcase(s):

# 	turn string_like_this into StringLikeThis
# 	return ''.join([word.capitalize() for word in s.split('_')])

# names = ['llano_kusuma_dewa','ujang_pardede','coki_dzulumat']

# print(camelcase(names))
"""


"""
# def add_no(func):

#     def names(nama,jurusan):
#         return [
#             str(i)+' '+func(n,j) for (i,n,j) in zip(
#                     range(len(nama)),
#                     nama,jurusan
#                 )
#         ]

#     return names

# @add_no
# def login(nama,jurusan):
#     return nama+' '+jurusan

# nama = ['llano','ujang','fikri','toni']
# jurusan = ['elketro','kimia','las','rpl']
# print(login(nama,jurusan))
"""

### decoator with argumen


# def pangkat(nilai):

# 	def decorator(func):

# 		def hasil(bil):
# 			return func(bil)**nilai

# 		return hasil

# 	return decorator
# 	# if callable(arg):
# 	# 	nilai = 2
# 	# 	return decorator(arg)
# 	# else:
# 	# 	return decorator


# @pangkat(2)
# def input_nilai(bil):
# 	return bil


# print(input_nilai(5))


##### class dalam decorator #######
# import random

# class Remember:

# 	def __init__(self,fnc):
# 		self.__fnc = fnc
# 		self.memory = []

# 	def __call__(self):
# 		h = self.__fnc()
# 		self.memory.append(h)
# 		return h

# 	def get_memory(self):
# 		return self.memory

# @Remember
# def random_odd_digit():
# 	return random.choice([1,2,3,4,53,2,1])

# print(random_odd_digit())
# print(random_odd_digit())
# print(random_odd_digit())
# print(random_odd_digit.get_memory())

## contoh lain 
# class Data:

# 	def __init__(self,login):
# 		self.__data = []
# 		self.__log = login
		
		
# 	def __call__(self,n,k):
# 		self.__n = n
# 		self.__k = k
# 		self.__status = self.__log(self.__n,self.__k)
# 		if self.__status:
# 			self.__data.append({'nama':n,'kelas':k})
# 		return 'data telah berhasil di input' if self.__status else 'gagal'

# 	def getData(self):
# 		return self.__data

# @Data
# def login(nama=False,kelas=False):
# 	return True if nama and kelas else False

# for nama,kelas in zip(['llano','ujang','nana',None],['XIE1','XILAS2','XIK1',None]):
# 	print(login(nama,kelas))
# print(login.getData())
