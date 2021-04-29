

class Siswa:

	def __init__(self,nama,kelas,nilai):
		self.__nama = nama
		self.__kelas = kelas
		self.__nilai = nilai

	def hasil(self):
		return {
		'nama':self.__nama,
		'kelas':self.__kelas,
		'nilai':self.__nilai
		}
	def getNama(self):
		return self.__nama

	def getKelas(self):
		return self.__kelas

	def getNilai(self):
		return self.__nilai


if __name__=='__main__':
	siswa1 = Siswa('llano','11 elektro 1',100)
	siswa2 = Siswa('ujang','10 Las 3',95)
	print(siswa1.hasil())
	print(siswa2.hasil())

























