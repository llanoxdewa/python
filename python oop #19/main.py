class Mangga:
    
    # magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah
        #print('membeli {} dengan jumlah {}'.format(self.nama,self.jumlah))

    def __repr__(self):
        return 'Debug - membeli {} dengan jumlah {}'.format(self.nama,self.jumlah)
    
    def __str__(self):
        return 'membeli {} dengan jumlah {}'.format(self.nama,self.jumlah)
    
    def __add__(self,objek):
        return 'total jumlah belanjaan adalah : {}'.format(self.jumlah + objek.jumlah)

    @property
    def __dict__(self):
        return 'objek ini memiliki atribute nama : {} dan juga jumlah : {}'.format(self.nama,self.jumlah)

    

belanja1 = Mangga('mangga harum',30)
belanja2 = Mangga('mangga dua',25)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)
