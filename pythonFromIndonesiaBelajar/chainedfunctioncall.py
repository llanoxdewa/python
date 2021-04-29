######### chained function call ##########

# def tambah(a,b):
    # return a + b
    
# def kali(a,b):
    # return a * b

# x,y = 10,20
# hasil = (tambah if True else kali)(x,y)
# print(hasil)
    
def kalkulator(x,y,z):
    if z == 'x':
        return x * y
    if z == '+':
        return x + y
    if x == '-':
        return x - y
    if x == '/':
        return x / y
def perbandingan(x,y,z):
    if z == '<':
        return x < y
    if z == '>':
        return x > y
    if z == '=':
        return x == y
        
x = int(input('masukan bilangan-1 >> '))
y = int(input('masukan bilangan-2 >> '))
z = str(input('masukan operasi perbandingan >> '))
hasil = (kalkulator if input('aritmatika or perbandingan >> ') == 'aritmatika' else perbandingan)(x,y,z)
print(hasil)
    
    

    