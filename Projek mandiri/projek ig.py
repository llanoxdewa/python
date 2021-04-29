"""
Rp. 5000/baris
Rp. 5000/halaman
jika pakai database Rp. 200.000
"""
nama_pelanggan,jumlah_baris,jumlah_halaman,opsi_data_base = [],[],[],[]
file_print = open('hasil.txt','w')
print("welcome to program market".center(40,'='))

while True:
	nama_pelanggan.append(input('\nmasukan nama anda >> '))
	jumlah_baris.append(int(input('masukan jumlah baris program yang akan dibuat >> ')))
	jumlah_halaman.append(int(input('masukan jumlah halaman program yang akan dibuat >> ')))
	opsi_data_base.append(input('menggunakan data base ? >> '))
	if input('selesai >> ') == 'yes':
		break

def jumlah_bayar(jumlah_halaman,jumlah_baris,opsi_data_base,nama_pelanggan):
	tarif_perbaris = 5000*jumlah_baris
	tarif_perhalaman = 5000*jumlah_halaman
	tarif_database = 200000 if opsi_data_base=='yes' else 0
	total_harga = tarif_database+tarif_perhalaman+tarif_perbaris
	return f"""
nama pelanggan   : 	{nama_pelanggan}
tarif parbaris   : 	{tarif_perbaris}
tarif perhalaman : 	{tarif_perhalaman}
tarif database 	 : 	{tarif_database} 
total harga      : 	{total_harga}
			"""
for jh,jb,opdb,nama in zip(jumlah_halaman,jumlah_baris,opsi_data_base,nama_pelanggan):
	print(jumlah_bayar(jh,jb,opdb,nama))
	file_print.write(jumlah_bayar(jh,jb,opdb,nama))

file_print.close()


