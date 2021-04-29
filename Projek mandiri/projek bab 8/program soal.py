########ok
from Soal import soal,kunci
import pprint,random,shelve

hasil_ujian = open('hasil-ujian\\hasil_ujian.py','a')
hasil = {}



print("PROGRAM UJIAN BERBASIS PYTHON".center(80,'='))


class Ujian:
	jawaban = {}
	nilai = 0
	def __init__(self,nama,kelas,jurusan):
		self.nama = nama
		self.kelas = kelas
		self.jurusan = jurusan

	def show_soal(self):
		for sal,kode in soal.items():
			print(sal)
			self.jawaban.setdefault(kode,input('jawaban >> ').upper())

	def pemeriksaan_soal(self):
		for kode,jwb in self.jawaban.items():
			if kunci[kode] == jwb:
				self.nilai += 10
		return f'nama {self.nama}\nkelas {self.kelas}\njurusan {self.jurusan}\nnilai {self.nilai}\n'

while True:
	try:
		nama = input('masukan nama anda >> ')
		kelas = input('masukan kelas anda >> ')
		jurusan = input('masukan jurusan anda >> ')
		siswa1 = Ujian(nama,kelas,jurusan)
		print('silahkan jawab dengan jujur dan benar !!'.upper().center(80,'#'))
		siswa1.show_soal()
		print(siswa1.pemeriksaan_soal())
		hasil.setdefault(nama,siswa1.pemeriksaan_soal())
		hasil_ujian.write('hasil = '+pprint.pformat(hasil))

	except (ValueError,TypeError):
		print('\njawaban tidak valid !!!'.center(80,'-'))
	if input('\nselesai ? >> ').lower() == 'yes':
		break


hasil_ujian.close()



































