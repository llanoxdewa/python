# koding break the code 
import string
sourceHuruf = [i for i in string.ascii_lowercase]
sourceAngka = [i for i in range(99999+1)]
def brutforce_coba_coba_tipepw_kata(sourceHuruf):
	password = str(input('masukan password kata min&max(10digit dan tanpa <spasi>) >> '))
	while len(password) != 10:
		print('password harus 10 digit !!!')
		password = str(input('masukan password kata min&max(10digit) >> '))
	passL = list(password)
	for i in sourceHuruf:
		print('loading...')
		if i == passL[0]:
			huruf1 = i 
		if i == passL[1]:
			huruf2 = i
		if i == passL[2]:
			huruf3 = i
		if i == passL[3]:
			huruf4 = i
		if i == passL[4]:
			huruf5 = i
		if i == passL[5]:
			huruf6 = i
		if i == passL[6]:
			huruf7 = i
		if i == passL[7]:
			huruf8 = i
		if i == passL[8]:
			huruf9 = i
		if i == passL[9]:
			huruf10 = i
	tebakan = huruf1+huruf2+huruf3+huruf4+huruf5+huruf6+huruf7+huruf8+huruf9+huruf10
	if tebakan == password:
		print(f'password adalah : {tebakan}')
	else:
		print('password tidak ditemukan') 
def brutforce_coba_coba_tipepw_angka(sourceAngka):
	password = int(input('masukan password (max5 digit >> '))
	for angka in sourceAngka:
		print('loading......')
		if angka == password:
			print(f'your password is {angka}')
			break
program = {
	'tipe angka':brutforce_coba_coba_tipepw_angka,
	'tipe huruf':brutforce_coba_coba_tipepw_kata
}
try:
	telaso = str(input('masukan tipe brutforce >> '))
	program[telaso](sourceHuruf if telaso == 'tipe huruf' else sourceAngka)
except KeyError:
	print('key tidak ada di menu : \n> tipe angka\n> tipe huruf')
