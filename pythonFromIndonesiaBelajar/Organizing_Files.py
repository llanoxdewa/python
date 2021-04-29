import shutil,os,zipfile


## shutil.copy
# contoh penggunaan / penulisan 
# shutil.copy(source, destination)
# os.chdir('d:\\llano\\python testing')
# shutil.copy('d:\\llano\\python testing\\test.py','d:\\llano\\git-hub')
# print('your file has been copy to destination')

## shutil.move
# contoh penulisan
# shutil.move(source, destination)
# shutil.move('d:\\hasil.txt','d:\\llano\\python testing')

## module send2trash
# import send2trash
# send2trash.send2trash(<path>)

### Compressing Files with the zipfile Module
## Reading ZIP Files
# (untuk mengetahui nama file didalam file zip yang telah ditentukan)
# import zipfile,os
# os.chdir('d:\\')
# contoh_zip = zipfile.ZipFile('data.zip')
# daftar_nama_file = contoh_zip.namelist()
# print(daftar_nama_file)
# (untuk mengetahui informasi file didalam file zip)
# ukuran = contoh_zip.getinfo('data.txt').file_size #(filename/file_size/compressed_size)
# print(ukuran)
# contoh_zip.close()
####################
# contoh program untuk mengetahui informasi file pada zip
# import zipfile,os
# os.chdir('d:\\test-zip')
# with zipfile.ZipFile('test-zip.zip') as ziip:
# 	for file in ziip.namelist():
# 		print(f"""file name : {file}\nfile size : {ziip.getinfo(file).file_size}\nfile compressed size : {ziip.getinfo(file).compress_size}\n""")
####################

## extracting from zip file
# (extractall) akan mengekstrack semua file yang ada pada zip file
# >>> import zipfile, os
# >>> os.chdir('C:\\') # move to the folder with example.zip
# >>> exampleZip = zipfile.ZipFile('example.zip')
# >>> exampleZip.extractall() or examplezip.extractall('<file hasilnya>'		)
# >>> exampleZip.close()
# (extracta(<file>)) hanya akan mengestract file yang dipilih
# >>> exampleZip.extract('spam.txt')
# 'C:\\spam.txt'
# >>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
# 'C:\\some\\new\\folders\\spam.txt'
# >>> exampleZip.close()

## Creating and Adding to ZIP Files
# >>> import zipfile
# >>> newZip = zipfile.ZipFile('new.zip', 'w')
# >>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# >>> newZip.close()
















