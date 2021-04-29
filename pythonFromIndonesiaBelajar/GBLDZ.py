####### menggabungkan beberapa list dengan fungsi zip list yang berkorelasi ########
listNama = ['llano','ujang','bejo','sumarti']
listAbsen = [12,29,1,4]
listNilai = [100,50,90,88]
siswa = list(zip(listNama,listNilai,listAbsen))
#siswa = [[i for i in listNama],[i for i in listAbsen],[i for i in listNilai]]
# for i in range(len(listNama)):
# 	siswa.append((listNama[i],listAbsen[i],listNilai[i]))
print(siswa)