# iterable adalah objek yang dapat dilakukan iterasi dan dapat menghasilkan iterator dengan menggunakan fungsi iter(iterable_objek)
# iterator adalah objek yang mengatur iterasi pada sekumpulan nilai (onbjek itetable)



l = [11,12,13,14]
x = iter(l)
x2 = iter(l)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x2))

# Generator 
# def generator(n):
#     i = 0
#     while(i < n):
#         yield i
#         i += 1
# for x in generator(5):
#     print(x)

# comprehension syntax
# cara lama / kuno
listganjil = []
for i in range(11):
    if i % 2 != 0:
        print('bilangan ganjil')
        listganjil.append(i)
# cara baru / modern
listgenap = [bilangan for bilangan in range(11) if bilangan % 2 == 0 ]
    
print(f'anggota bilangan ganjil {listganjil}')
print(f'anggota bilangan genap {listgenap}')

name = ['llano','boedi','udil','random','bambang']
d = {no : nama for no in range(1,6) for nama in name}
print(d)

    
