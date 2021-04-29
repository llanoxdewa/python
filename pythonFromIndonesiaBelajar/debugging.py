


# penggunaan raise
# raise Exception('error')

# def input_data(nama,kelas,nilai):
# 	if len(nama) < 8:
# 		raise Exception('panjang nama harus >= 8')
# 	return f'nama : {nama} \nkelas : {kelas} \nnilai : {nilai}'

# siswa = input_data('llano','XIE1',100)
# print(siswa)

## contoh penggunaan try dan except

# def data(nama):
# 	return f'selamat malam {nama}'
# try:
# 	hasil = data('llano','ujang')
# 	print(hasil)
# except Exception as err:
# 	print(f'terdapat error yaitu "{err}"')


## Getting the Traceback as a String
# def sam():
# 	return nama()
# def nama():
# 	return 'wlwl'

# print(sam())

# import traceback
# try:
# 	raise Exception('This is the error message.')
# except:
# 	errorFile = open('errorInfo.txt', 'w')
# 	errorFile.write(traceback.format_exc())
# 	errorFile.close()
# 	print('The traceback info was written to errorInfo.txt.')

## assertions
# assert <condition>,<optional-message or method>
# podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# kata = True
# assert kata == True, 'kata tidak true'
# nama = ['ujang','llano','bambang','taroi']

# for name in nama:
# 	assert len(name)>=5,f'pangjang nama {name} kurang dari 5'


## logging ##

import logging

# ada 5 jenis logging
"""
DEBUG(10) : Detailed information, typically of interest nly when diagnosing problem
INFO(20) : Confirmation that thing are working as expected
WARNING(50): An indication that something unpected happened, or indcative of some
problem in near future. 
ERROR(40) : The software has not been able to perform some function
CRITICAL(50) : A serious error, indicating that the program itself may be unable to continue running.

"""
# def tambah(bil1,bil2):
# 	return bil1 + bil2

# def kurang(bil1,bil2):
# 	return bil1 - bil2

# def bagi(bil1,bil2):
# 	return bil1 / bil2

# def kali(bil1,bil2):
# 	return bil1 * bil2 

# bil1 = 10
# bil2 = 3
# logging.basicConfig(level=logging.INFO,
# 	format='%(levelname)s:bilangan telah di lakukan operasi aritmatika%(message)s')


# logging.info('hasil {} + {} = {}'.format(bil1,bil2,tambah(bil1,bil2)))
# logging.info('hasil {} x {} = {}'.format(bil1,bil2,kali(bil1,bil2)))
# logging.info('hasil {} - {} = {}'.format(bil1,bil2,kurang(bil1,bil2)))
# logging.info('hasil {} / {} = {}'.format(bil1,bil2,bagi(bil1,bil2)))

# disable logging
# >>> import logging
# >>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
# Debugging 225
# >>> logging.critical('Critical error! Critical error!')
# 2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
# >>> logging.disable(logging.CRITICAL)
# >>> logging.critical('Critical error! Critical error!')
# >>> logging.error('Error! Error!')


# Logging to a File
# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
















