# operasi bitwyse

a = 9
b = 5

# bitwise or (|)
print('\n',17*'=','or', '\n')
c = a | b 
print('nilai :', a, 'binary :', format(a,'08b'))
print('nilai :', b, 'binary :', format(b,'08b'))
print(18*'-','(|)')
print('nilai :',c,' , binary :', format(c, '08b'))

# bitwise and(&)
print('\n',17*'=','and', '\n')
c = a & b
print('nilai :', a, 'binary :', format(a,'08b'))
print('nilai :', b, 'binary :', format(b,'08b'))
print(18*'-','(&)')
print('nilai :',c,' , binary :', format(c, '08b'))

# bitwise xor(^)
print('\n',17*'=','xor', '\n')
c = a ^ b
print('nilai :', a, 'binary :', format(a,'08b'))
print('nilai :', b, 'binary :', format(b,'08b'))
print(18*'-','(^)')
print('nilai :',c,' , binary :', format(c, '08b'))

# bitwise not(~)
print('\n',17*'=','not', '\n')
c = ~a
print('nilai :', a, 'binary :', format(a,'08b'))
print('nilai :',c,' , binary :', format(c, '08b'))
d = 0b0000001001
e = 0b1111111111
print('\n',17*'=','di xor kan', '\n')
print('nilai :',e^d,' , binary :', format(e^d, '08b'))

# shifting rigt (>>)
c = a >> 3
print('\n', 12*'=','>>', 12*'=','\n')
print('nilai :', a, 'binary :', format(a,'08b'))
print(18*'-','(>>)')
print('nilai :',c,' , binary :', format(c, '08b'))

# shifting left (<<)
c = a << 3
print('\n', 12*'=','>>', 12*'=','\n')
print('nilai :', a, 'binary :', format(a,'08b'))
print(18*'-','(>>)')
print('nilai :',c,' , binary :', format(c, '08b'))




