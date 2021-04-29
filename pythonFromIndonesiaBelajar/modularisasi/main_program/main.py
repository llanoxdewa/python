from modul.operasi import *

bil1 = int(input('bil 1 >> '))
bil2 = int(input('bil 2 >> '))
operasi = input('operasi >> ')
bilangan = Operasi(bil1,bil2)
ops = {'kali':bilangan.kali,
	   'bagi':bilangan.bagi,
	   'kurang':bilangan.kurang,
	   'tambah':bilangan.tambah,
	  '>':bilangan.lebih_besar,
	  '<':bilangan.lebih_kecil,
	  '=':bilangan.sama_dengan,
	   }

print(ops[operasi]())









