# INHARITANCE 

class Person:
    def __init__(self,nama = 'no nama', umur = 0):
        self.__nama = nama
        self.__umur = umur
    def getNama(self):
        return self.__nama
    def getUmur(self):
        return self.__umur
    def perkenalkan(self):
        return f'\nnama : {self.__nama} \numur : {self.__umur} tahun'
    
class Murid(Person):
    def __init__(self, nama = 'no nama',umur = 0,Id = 3233):
        super().__init__(nama = nama,umur = umur)
        self.id = Id
    def perkenalkan_murid(self):
        return f'\nnama murid : {self.getNama()} \numur : {self.getUmur()} \nNo.ID : {self.id}'
class Guru(Person):
    def __init__(self, nama = 'no nama',umur = 0,pelajaran = 'no mapel'):
        super().__init__(nama = nama,umur = umur)
        self.pelajaran = pelajaran
    def perkenalkan_guru(self):
        return f'\nnama Guru : {self.getNama()} \nberumur : {self.getUmur()} \nmengajar mata pelajaran : {self.pelajaran}'
       
G = Guru('bu rofi',17,'matematika')
M = Murid('llano',12,101905925)
print(M.perkenalkan_murid())
print(G.perkenalkan_guru())