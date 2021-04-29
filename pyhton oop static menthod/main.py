class Hero:

    # private class varibel
    __jumlah = 0;
    
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # hanya berlakku untuk objek
    def getjumlah0(self):
        return Hero.__jumlah

    # hanya berlaku untuk class
    def getJumlah():
        return Hero.__jumlah

    # membuat static menthod (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah1():
        return Hero.__jumlah
    
    # hanya berlaku untuk class
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
 



fanny = Hero('fanny')
print(Hero.getJumlah1())
lancelot = Hero('lancelot')
print(Hero.getJumlah1())
hayabusa = Hero('hayabusa')
print(Hero.getJumlah3())