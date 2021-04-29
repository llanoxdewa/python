# operasi dan manipulasi string

# 1. menyambung string (concanate)
nama_pertama = "lutfy"
nama_tengah = "D"
nama_akhir = "monkey"

nama_lengkap = nama_pertama +" "+ nama_tengah+"'"+ nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print('panjang dari' +''+ nama_lengkap + '=' + str(panjang))

# 3. operator pada string

# mengecek apakah ada komponen char atau string di string

d = "D"
status = d in nama_lengkap
print('string ' + d + " ada di " + nama_lengkap +" "+ str(status))

D = "d"
status = D not in nama_lengkap
print('string ' + D + " tidak ada di  " + nama_lengkap +" "+ str(status))

# mengulang string
print('wk'*14)

# indexing
print('index ke-0 : ' + nama_lengkap[0])
print('index ke-0 : ' + nama_lengkap[1])
print('index ke-0 : ' + nama_lengkap[13])
print("index ke-[0:3] :" + nama_lengkap[0:4])
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil :" + min(nama_lengkap))
# item paling besar
print("paling besar :" + max(nama_lengkap))

ascii_code = ord("u")
print("ASCII code untuk spasi adalah :", str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah :", chr(data))

# operator dalam bentuk menthod
data = "ucup sarucup tircup"
jumlah = data.count("u")
print("jumlah o dalam " + data +" = "+ str(jumlah))

