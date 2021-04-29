class Data:

	data_diri = open('data diri.txt','r')
	data_nilai = open('data nilai.txt','r')
	data_jadwal = open('data jadwal.txt','r')
	daftar_data = {
	'data diri':data_diri,
	'data nilai':data_nilai,
	'jadwal':data_jadwal
	}

	def show_data(self):
		pilih = str(input('\n\nmasukan data yang ingin di buka >> '))
		print('\n',self.daftar_data[pilih].read())
		self.data_nilai.seek(0)
		self.data_jadwal.seek(0)
		self.data_diri.seek(0)

if __name__ == '__main__':
	a = Data()
	a.show_data()

