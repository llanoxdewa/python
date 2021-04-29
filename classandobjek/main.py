# class and objek in python 

class Segiempat:
    # field = apa yang dimiliki oleh class --> kata benda / noun
    # method = apa yang dapat dilakukan oleh class --> kata kerja / verb
    panjang = 0
    lebar = 0
    def hitungLuas(self):
        self.panjang  
        self.lebar 
        return self.panjang * self.lebar
try:
    bangundatar = Segiempat()
    bangundatar.panjang = int(input('masukan panjang >> '))
    bangundatar.lebar = int(input('masukan lebar >> '))
    print(bangundatar.hitungLuas())
except ValueError:
    print('input harus bilangan')
    



