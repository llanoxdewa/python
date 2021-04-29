# a = 10 , a adalah tipe data bernilai 10

#tipe data : angka
data_integer = 2 

print("data :", data_integer)
print(" -bertipe :", type(data_integer))

# tipe data : angka dengan koma(float)
data_float = 2.4
print("data :", data_float)
print(" -bertipe :", type(data_float))

# tipe data dari kumpukan carakter (string)
data_string = "cupu"
print("data :", data_string)
print(" -bertipe :", type(data_string))

# tipe data : biner true/false (bolean)
data_bool = True 
print("data :", data_bool)
print(" -bertipe :", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,4)
print("data :", data_complex)
print(" -bertipe :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print(" -bertipe :", type(data_c_double))







