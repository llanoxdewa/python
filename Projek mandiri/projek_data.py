from prettytable import PrettyTable as PT


Tabel_Data = PT()
Colom_Data = ['nama','kelas','jurusan','nilai']
nama,kelas,jurusan,nilai = [],[],[],[]
while True:
	nama.append(str(input('masukan nama >> ')))
	kelas.append(int(input('masukan kelas >> ')))
	jurusan.append(str(input('masukan jurusan >> ')))
	nilai.append(int(input('masukan nilai >> ')))
	if input('selesai >> ') == 'yes':
		break
print('\n\n')
def inputData(nama,kelas,jurusan,nilai):
	Tabel_Data.add_column(Colom_Data[0],nama)
	Tabel_Data.add_column(Colom_Data[1],kelas)
	Tabel_Data.add_column(Colom_Data[2],jurusan)
	Tabel_Data.add_column(Colom_Data[3],nilai)
	print(Tabel_Data)

inputData(nama,kelas,jurusan,nilai)





