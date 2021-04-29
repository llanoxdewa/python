# abstrak class
from abc import ABCMeta, abstractmethod

class BangunDatar(metaclass = ABCMeta):
    @abstractmethod
    def get_luas(self):
        "return luas bangun datar"
    @abstractmethod
    def get_alas(self):
        'return alas'
    @abstractmethod
    def get_tinggi(self):
        'return tinggi'
        
    def __str__(self):
        return "luas bangun ini adalah  " + str(self.get_luas())
    def __add__(self,other):
        n = Segitiga(self.get_alas() + other.get_alas(), self.get_tinggi() + other.get_tinggi())
        return n  
class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas,self.tinggi = alas,tinggi
    def get_alas(self):
        return self.alas
    def get_tinggi(self):
        return self.tinggi
    def get_luas(self):
        return (self.alas * self.tinggi) / 2
        

segitiga1 = Segitiga(12,4)
segitiga2 = Segitiga(3,1)
segitiga3 = segitiga1 + segitiga2
print(str(segitiga3))