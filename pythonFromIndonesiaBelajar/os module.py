# cara menulis dan membaca file menggunakan bahasa pemograman python
import os,shelve
# data = ['test.py','hasil.txt','segitiga.py']

#for file in data:print(os.path.join(f"D:\\llano\\python testing>{file}"))

## getcwd and chdir
# getcwd untuk melihat kita sedang berada di direktori mana 
# chdir untuk berpindah directory
# print(os.getcwd())
# os.chdir('D:\\llano\\python testing')
# print(os.getcwd())

## os.makedirs()
# berfungsi untuk membuat folder directory baru
# nama_f = input('masukan nama folder >> ')
# os.makedirs(f'd:\\llano\\python testing\\{nama_f}')


			# pengertian absolute path dan relative path #
"""
Absolute Path
Absolute path artinya path ditulis dengan lengkap dari nama parent 
directory sampai nama filenya. Misal, /home/tux/aloha.txt

Relative Path
Relative path artinya path tidak ditulis lengkap, tetapi berdasarkan 
posisi direktori yang sedang anda akses atau sering disebut direktori kerja
atau working directory. Misal, saat ini anda berada di direktori /home/
"""


## os.path
# os.path.abspath('.')
# print(os.path.abspath('.'))
# print(os.path.abspath('.\\src'))
# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.\\src')))

# os.path.relpath(<directory>,<director sebelum directory kerja>)
# print(os.path.relpath('d:\\pythonfromindonesiabelajar', 'd:\\llano\\python'))
# print(os.getcwd())


## os base name and dirname
# path = 'd:\\llano\\python testing\\test.py'
# print(os.path.basename(path)) # akan mereturn nama file pada directory tersebut
# print(os.path.dirname(path)) # akan mereturn absolutepath file tersebut berada
# Jika Anda membutuhkan nama dir jalur dan nama dasar bersama-sama, Anda bisa menelepon
# os.path.split () untuk mendapatkan nilai tuple dengan dua string ini
# testFilePath = 'd:\\llano\\python testing\\test.py'
# print(os.path.split(testFilePath))
# gunakan <file>.split(os.path.sep) jika ingin mereturn list 
# print(testFilePath.split(os.path.sep))

## os.path.getsize(<path>) dan os.listdir(<path>)
# os.path.getsize() = berfungsi untuk mereturn ukuran file dalam suatu path
# os.listdir() = untuk mereturn list file yang ada didalam suatu directory
# print(os.path.getsize(testFilePath))
# print(os.listdir(os.path.dirname(testFilePath)))

## os.path.isdir()/isfile()/exists()
# os.path.exists() --> akan mereteturn true jika file atau folder yang dirujuk ada dan sebaliknya
# print(os.path.exists('d:\\llano'))
# os.path.isdir() --> akan mereturn true jika argumen yang dirujuk berupa directory/folder
# print(os.path.isdir('d:\\llano\\python testing'))
# os.path.isfile() --> akan mereturn true jika argumen yang dirujuk berupa file 
# print(os.path.isfile('d:\\llano\\python testing\\test.py'))

## fungsi module os untuk menghapus file/folder pada suatu path
# os.unlink(path) --> untuk menghapus file pada suatu path / directory
# os.rmdir(path) --> untuk menghapus suatu folder / directory
# os.rmtree(path) --> untuk menghapus file dan direcotory

## fungsi module os untuk mengetahui folder apa saja yg ada di path kita
# for folderName, subfolders, filenames in os.walk('d:\\llano\\python'):
# 	print('The current folder is ' + folderName)
# 	for subfolder in subfolders:
# 		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
# 	for filename in filenames:
# 		print(f'filename of {folderName} : {filename}')

## cara membaca dan menulis file 
# 'w' untuk menulis dengan fungsi write()
# 'r' untuk membaca file dengan fungsi read()
# 'a' untuk menambahkan isi file dengan fungsi write()
# fungsi readline() --> untuk mengembalikan list sesuai baris pada suatu file
# >> contoh
"""
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
"""
# sonnetFile = open('sonnet29.txt')
# sonnetFile.readlines()
# ["""When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
# outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
# look upon myself and curse my fate,"""]

# hasil_w = open('d:\\llano\\python testing\\hasil.txt','a')
# hasil_w.write('hello world')
# hasil_r = open('d:\\llano\\python testing\\hasil.txt','r')
# hasil_isi = hasil_r.read()
# print(hasil_isi)
# hasil_r.close()
# hasil_w.close()

## Saving Variables with the shelve Module
# untuk mengatur key dan valuenya pada shelve file
# shelfile = shelve.open('mydata')
# cats = ['angora','black cat','white cat','brown cat']
# shelfile['cats'] = cats
# untuk melihat keys dan values yang tersimpan di shelfile
# print(list(shelfile.keys()))
# print(list(shelfile.values()))
# shelfile.close()

## menyimpan variabel dengan pprint
"""
pprint.pformat() akan menampilkan format data suatu variabel (list,dict,dll)
"""
# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# pprint.pformat(cats)
# fileObj = open('myCats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')










