####### cara yang lebih pythonic dengan menggunakan fungsi zip

jurusan = ['elektro','kimia','las']
nama = ['llano','ujang','bejo']
kelas = [11,12,10]
hobi = ['main komputer','main game','baca buku']

for d_jurusan,d_nama,d_hobi,d_kelas in zip(jurusan,nama,hobi,kelas):
    print(f'nama    : {d_nama}\nkelas   : {d_kelas}\njurusan : {d_jurusan}\nhobi    : {d_hobi}\n')