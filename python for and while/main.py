n = int(input('masukan banyak bilangan rata-rata? :'))
data = 0
batas = 1

#while(batas <= n):
#    print('masukan bilangan ke-',batas)
#    data += int(input())
#    batas += 1

for i in range(1,n+1):
    print('masukan bilangan ke-',i)
    data += int(input())
    
data /= n
print('\nhasil rata rata adalah :',data)