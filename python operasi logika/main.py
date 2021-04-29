# operasi logika

# not,or, and, xor

print('====NOT====')
a = True
b = 1
c = not b
print('data a =', a)
print('data b =', b)
print('--------NOT')
print('data c =', c)

# AND (jika dua buah nilai true, maka akan bernilai True)
print('====AND====')
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

# xor (akan true jika ada salah satu maka akan true jika true 22 nya akan false)
print('====xor====')
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)

# or (jika salah satu true maka akan true)
print('====or====')
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

























