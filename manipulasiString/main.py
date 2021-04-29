# # operasi dan manipulasi string
# # operator dalam bentuk method
# #merubah semua ke upper case

# salam = "tod"
# print('normal = '+ salam)
# salam = salam.upper()
# print('upper = ' + salam)
# kimak = 'Aku Tidak Sudi SEKALI'
# print('normal = ' + kimak)
# kimak = kimak.lower()
# print('lower = ' + kimak)

# # pengecekan dengan menggunakan method
# # contoh untuk pengencekan lower chase

# salam = str(input('masukan kata >>> '))
# apakah_lower = salam.islower()
# print(salam + ' apakah lower ?  ' + str(apakah_lower))
# apakah_upper = salam.isupper()
# print(salam + ' apakah upper  ' + str(apakah_upper))


# # is alpha () <--- untuk mengecek apakah semuanya angka
# # isnum() <--- huruf dan angka
# # isdecimal() <--- angka saja
# # isspace() <--- spasi, tab, newline \n
# # istitle() <--- semua kata dimulai dengan huruf besar

# judul = "It Is Okay Not To Be Hokage"
# cek_judul = judul.istitle()
# print('apakah' + judul + 'is title ? ' + str(cek_judul))


# ## ngecek komponen startswith() endswith() <--- keren
# cek_start = "Kimak Anda dan juga anda tidak kompeten".startswith("Kimak")
# cek_end = "Kimak Anda dan juga anda tidak kompeten".endswith("kompeten")
# print("start = " + str(cek_start))
# print("end = " + str(cek_end))


# # penggabungan komponen join() dan split()
# pisah = ['aku', 'saya', 'kita']
# gabungan = ' --> '.join(pisah)
# print(gabungan)
# # split()
# gabungan = "Duniakkadalahkktempatkksunyi"
# print(gabungan.split('kk'))

# # alokasi karakter rjust(), ljust(), center()
# print(5*'>' + ' welcome to mobile legend ' + 5*'<')
# kanan = "kanan".rjust(10)   
# print("'"+kanan+"'")
# kiri = "kiri".ljust(10)
# print("'"+kiri+"'") 
# tengah = "tengah".center(10,'-')
# print("'"+tengah+"'") 
# # print("tengah".center(20,'-'))
# #  strip() <--- berfungsi untuk menghilangkan efek dari yang di atas
# tengah = tengah.strip('-')
# print(tengah)

password = input('masukan password >>> ')
cek_pw = password.isdecimal()
if cek_pw == False:
    print('password harus angka')
else:
    print('password anda benar')
    for i in range(1,11):
        print('mantap')
        

