def tambah(bil1, bil2):
    nilai = bil1 + bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",nilai)
 
def kondisi(nilai_ujian_satu, nilai_ujian_dua):
    hasil = (nilai_ujian_satu + nilai_ujian_dua)/2
 
    if hasil >= 70:
        print("nilai anda",hasil,"maka anda lulus")
 
    else:
        print("nilai anda",hasil,"maka anda harus remedial")
        
def pangkat(dasar,pangkat):
    print(f'{dasar} pangkat {pangkat} adalah : {dasar**pangkat}')

tambah(12,5)
if __name__ == '__main__':
    pangkat(4,2)
    tambah(12,4)
    kondisi(90,89)
    