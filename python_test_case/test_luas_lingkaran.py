import unittest
from math import pi
from luas_lingkaran import count_luas_lingkaran
class Test_luas_lingkaran(unittest.TestCase):
	
	def test_hasil(self):
		# test hasil saat bilangan positif atau >=0
		for value in [v for v in range(1,100)]:
			self.assertAlmostEqual(count_luas_lingkaran(value),pi*value**2)
			
	def test_value(self):
		self.assertRaises(ValueError,count_luas_lingkaran,-1)
	
	def type_value(self):
		self.assertRaises(TypeError,count_luas_lingkaran,True)
	

if __name__=='__main__':
	unittest.main()












