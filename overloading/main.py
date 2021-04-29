class Person:

    def __init__(self,nama = 'no nama', umur = 0):
        self.__nama = nama
        self.__umur = umur if umur > 0 else 0
    def perkenalan(self):
        return f'nama saya : {self.__nama} \numur saya : {self.__umur}'
    def getNama(self):
        return self.__nama
    def getUmur(self):
        return self.__umur
    # operator overloading
    def __add__(self, other):
        n = Person(self.getNama() + other.getNama(), self.getUmur() + other.getUmur())
        return n
    def __str__(self):
        return self.perkenalan() + "  ini telah ditambahkan"

def main():
   p = Person('ujang',16)
   y = Person('bayu',20)
   a = p + y
   print(a.perkenalan())
   print(str(a))



main()