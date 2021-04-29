# operasi ditambah dengan assigment
# operasi aritmatika
a = 5 # adalah assigment
print('nilai a :', a)

a += 1 # artinya a = a + 1
print('nilai a += 1 :', a)

a -= 2 # artinya a = a - 2
print('nilai a -= 2 :', a)

a *= 5 # artinya a = a * 4
print('nilai a *= 4 :', a)

a /= 2 # artinya a = a / 5
print('nilai a /= 5 :', a)

b = 10
print("\nnilai b :", b)

# operasi modulus dan floor division
b //= 3
print('nilai b //= 3 :', b)

# operasi perpangkatan / eksponen
a = 5
print('\nnilai a :', a)
a **= 3
print('nilai a **= 3 :', a)

# operasi bitwise
# OR
c = True
print('nilai c :', c)
c |= False
print('nilai c |= false :', c)
c = False
print('nilai c :', c)
c |= False
print('nilai c |= false :', c)

# AND
c = True
print('\nnilai c :', c)
c &= False
print('nilai c &= false :', c)
c = True
print('nilai c :', c)
c &= True
print('nilai c &= true :', c)

# XOR
c = True
print('\nnilai c :', c)
c ^= False
print('nilai c ^= false :', c)
c = True
print('nilai c :', c)
c ^= True
print('nilai c ^= true :', c)

# shifting
d = 0b0100
print('\nnilai d :',format(d, '04b'))
d >>= 2
print('nilai d >>=2',format(d, '04b'))



