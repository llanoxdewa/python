class Pemalas:

    def __init__(self, inama, iumur, ihobi):
        self.nama = inama
        self.umur = iumur
        self.hobi = ihobi
    # void function dengan method dan tanpa parameter
    def siapa(self):
        print('nama saya adalah ' + self.nama)
    # method dengan argumen
    def upUmur(self, up):
        self.umur += up
    # method dengan return
    def kembali(self):
        return self.hobi

        

pemalas1 = Pemalas('llano', 16, 'nonton anime')
pemalas2 = Pemalas('bujang', 17, 'nonton film')

pemalas1.siapa()
print(pemalas1.umur)
pemalas1.upUmur(3)
print(pemalas1.umur)
pemalas2.siapa()
print(pemalas1.kembali())



