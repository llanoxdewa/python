class NamaLengkap:

    def namaAja(self, nama):
        self.__nama = nama
        return self.__nama
    
    def __namaLengkap(self):
        return f'nama saya {self.__nama}'
    def __add__(self,other):
        n = NamaLengkap()
        namaL = n.namaAja(self.__nama + other.__nama)
        return namaL

d = NamaLengkap()
b = NamaLengkap()
d.namaAja('llano ')
b.namaAja('kusuma dewa')
lp = d + b
print(lp)
        
        