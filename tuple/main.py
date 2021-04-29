
## tuple merupakan data yang bersifat imutable atau elemen 


tuple = (1,2,3,4,5,6,7)
print(f'tuple ku : {tuple}')
tuple = list(tuple)
tuplemu = (54,7.4,False,"kntl",[i for i in tuple])
print(f'tuple mu : {tuplemu}')
tuple = (1,2,3,4,5,6,7)
print(f'data ke 2 dari tuple adalah : {tuple[4:]}')
# tuple[2] = 69 <-- nilai data dari tuple tidak dapat di ubah
# penjumlahan tuple
tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)
print(f'gabungan dua tuple {tuple1 + tuple2}')
