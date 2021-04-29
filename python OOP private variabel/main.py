class Hero:

    #class variabel
    jumlah = 0
    # class private variabel
    __privatejumlah = 0

    def __init__(self, nama, darah):
        self.nama = nama
        self.darah = darah

        # variabel instance private
        self.__private = 'private'
        # variabel instacne protecte
        self._protected = 'protected'

chou = Hero('chou', 100)

print(chou.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)
