class Person:

    def __init__(self, nama, kelas, jurusan):
    
        self.__nama = nama
        self.__setKelas(kelas)
        self.__jurusan = jurusan

    def __setKelas(self,kelas):
        self.__kelas = 11
        return self.__kelas
    def getNama(self):
        return self.__nama
    def getKelas(self):
        return self.__kelas
    def getJurusan(self):
        return self.__jurusan

nama = str(input('nama >>'))
kelas = int(input('kelas >>'))
jurusan = str(input('jurusan >>'))
orang = Person(nama,kelas,jurusan)

print(f'nama : {orang.getNama()}')
print(f'kelas : {orang.getKelas()}')
print(f'jurusan : {orang.getJurusan()}')