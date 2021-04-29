# def jumlahkan(p_satu,p_dua):
# 	return p_satu + p_dua
# listku = [4,5]
# dictku = {
# 	'p_satu':100,
# 	'p_dua':200
# }
# hasil_list = jumlahkan(*listku)
# print(f'jumlah dari list : {hasil_list}')
# hasil_dict = jumlahkan(**dictku)
# print(f'jumalh dari dictku : {hasil_dict}')
def view(nama,nilai,No):
	for nama,nilai,no in zip(nama,nilai,No):
		print(f'\nnama : {nama}\nNoPerserta perserta : {no}\nmendapatkan nilai : {nilai}')
	
namaPerserta = ['llano','ujang','bejo','hari']
nilaiUjian = [95,100,89,78]
NoPerserta = ['1101101','1101291','1012000','1010101']
mydata = {
	'nama':namaPerserta,
	'nilai':nilaiUjian,
	'No':NoPerserta
}
hasil = view(**mydata)


