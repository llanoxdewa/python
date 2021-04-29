# Encapsulasi 
class Person:
    __umur = 0
    def __init__(self, name = 'no name', umur = 'no umur'):
        self.__nama = name
        self.__setUmur(umur) 
    def getName(self):
        return self.__nama
    def getUmur(self):
        return self.__umur
    #     return self.__umur
    def __setUmur(self, umur):
        c = 'umur tidak valid'
        self.__umur = umur if umur > 0 else c
        return self.__umur
s = str(input('masukan nama :'))
u = int(input('masukan umur anda :'))
p = Person(s,u)

print(p.getName())
print(p.getUmur())