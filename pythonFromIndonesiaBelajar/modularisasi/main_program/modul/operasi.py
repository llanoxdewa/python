class Operasi:
	def __init__(self,bil1,bil2,perbandingan=None):
		self.bil1 = bil1
		self.bil2 = bil2
		self.perbandingan = perbandingan
	def kali(self):
		return f'hasil kali dari {self.bil1} dengan {self.bil2} adalah {self.bil1 * self.bil2}'

	def tambah(self):
		return f'hasil tambah dari {self.bil1} dengan {self.bil2} adalah {self.bil1 + self.bil2}'

	def kurang(self):
		return f'hasil kurang dari {self.bil1} dengan {self.bil2} adalah {self.bil1 - self.bil2}'

	def bagi(self):
		return f'hasil bagi dari {self.bil1} dengan {self.bil2} adalah {self.bil1 * self.bil2}'


	def lebih_besar(self):
		return 'benar' if self.bil1 > self.bil2 else 'salah'
	def lebih_kecil(self):
		return 'benar' if self.bil1 < self.bil2 else 'salah'
	def sama_dengan(self):
		return 'benar' if self.bil1 == self.bil2 else 'salah'



