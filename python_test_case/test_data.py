import unittest
from Data import Siswa

class testDataSiswa(unittest.TestCase):




	def setUp(self):
		self.siswa1 = Siswa('llano','XIE1',100)
		self.siswa2 = Siswa('ujang','XILAS2',90)
		print('set up data.....')
	def tearDown(self):
		print('test is done and succes!!!\n')
	def test_returnData(self):
		self.assertEqual(self.siswa1.hasil(),{'nama':'llano','kelas':'XIE1','nilai':100})
		self.assertEqual(self.siswa2.hasil(),{'nama':'ujang','kelas':'XILAS2','nilai':90})
	def test_returnNama(self):
		self.assertEqual(self.siswa1.getNama(),'llano')
		self.assertEqual(self.siswa2.getNama(),'ujang')

	def test_returnKelas(self):
		self.assertEqual(self.siswa1.getKelas(),'XIE1')
		self.assertEqual(self.siswa2.getKelas(),'XILAS2')
	def test_returnNilai(self):
		self.assertEqual(self.siswa1.getNilai(),100)
		self.assertEqual(self.siswa2.getNilai(),90)


if __name__=='__main__':
	unittest.main()


































