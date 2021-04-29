# # kecepatan = [i for i in range(20,121,10)]
# # print(kecepatan)
# # ambang_batas = int(input('>> '))
# # for laju in kecepatan:
# # 	if laju > ambang_batas:
# # 		print('kecepatan melewati ambang batas')
# # 		break
# # else:
# # 	print('kecepatan normal')
# # 	
# list_nilai = [i for i in range(10,101,10)]
# KKM = int(input('input KKM >> '))
# for i in list_nilai:
# 	if i < KKM:
# 		print(f'nilai anda ada yang dibawah KKM yaitu {list(i for i in list_nilai if i < KKM)}')
# 		break
# else:
# 	print('nilai anda tidak ada yang dibawah KKM')


# listnilai = [80,55,33,66,77,78,56,90,100,100,90,60,44]
# listDibawahKKM = [i for i in listnilai if i < 0]
# if len(listDibawahKKM) == 0:
# 	print('nilai tidak ada yang dibawah KKM')
# elif len(listDibawahKKM) != 0:
# 	print(f'nilai ada yang di bawah KKM yaitu {listDibawahKKM}')