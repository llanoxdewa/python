# belajar casting 
# merubah dari satu tipe data ke tipe data lain
# tipe data = int, float, str, bool

## INTERGER
print("============integer==========")
data_int = 12 
print("data = ", data_int, "type data = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan bernilai false jika data int bernilai = 0 

print("data = ", data_float, "type data = ", type(data_float))
print("data = ", data_str, "type data = ", type(data_str))
print("data = ", data_bool, "type data = ", type(data_bool))

## float
print("============float==========")
data_float = 9.9
print("data = ", data_float, "type data = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan bernilai false jika data int/float  bernilai = 0 

print("data = ", data_int, "type data = ", type(data_int))
print("data = ", data_str, "type data = ", type(data_str))
print("data = ", data_bool, "type data = ", type(data_bool))

## boolean
print("============boolean==========")
data_bool = False
print("data = ", data_bool, "type data = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)  

print("data = ", data_int, "type data = ", type(data_int))
print("data = ", data_str, "type data = ", type(data_str))
print("data = ", data_float, "type data = ", type(data_float))

## string
print("============string==========")
data_str = "19"
print("data = ", data_str, "type data = ", type(data_str))

data_int = int(data_str)# string harus angka
data_bool = bool(data_str)# jika string kososong("") maka akan bernilai false
data_float = float(data_str) # string harus berupa angka 

print("data = ", data_int, "type data = ", type(data_int))
print("data = ", data_bool, "type data = ", type(data_bool))
print("data = ", data_float, "type data = ", type(data_float))

