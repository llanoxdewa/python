from DataPerpustakaan import Data


print('	welcome to program open data '.center(60,'*'))


while True:
	DP = Data()
	DP.show_data()
	if input('exit >> ') == 'yes':
		Data.data_diri.close()
		Data.data_jadwal.close()
		Data.data_jadwal.close()
		break

