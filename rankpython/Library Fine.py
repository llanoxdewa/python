
 # jika buku dikembalikan sebelum tanggal jatuh tempo tidak akan dikenakan denda
 # jika buku dikembalikan terlambat dikembalikan tapi masih dalam bulan yang sama denda = 15 hackos x (banyak hari terlambat)
 # jika buku dikembalikan lewat bulan denda = 500hackos x (bulan keterlambatannya)
 # jika buku dikembalikan lewat tahun denda = 10000hackos

# sampel input 
tanggal_dikembalikan = '9 6 2020'
jatuh_tempo = '6 6 2020'

def count_denda(td,jt):
	tanggal_dikembalikan,jatuh_tempo = [int(x) for x in td.split()],[int(x) for x in jt.split()]
	denda = 0
	if tanggal_dikembalikan[0]==jatuh_tempo[0] and tanggal_dikembalikan[1]==jatuh_tempo[1] and tanggal_dikembalikan[2]==jatuh_tempo[2]:
		return f'tidak ada denda'
	elif tanggal_dikembalikan[0]>jatuh_tempo[0]:denda += (tanggal_dikembalikan[0]-jatuh_tempo[0])*15
	elif tanggal_dikembalikan[1]>jatuh_tempo[1]:denda += (tanggal_dikembalikan[1]-jatuh_tempo[1])*500
	elif tanggal_dikembalikan[2]!=jatuh_tempo[2]:denda += 10_000
	return denda
print(count_denda(tanggal_dikembalikan,jatuh_tempo))