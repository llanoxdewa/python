class hero :
    # class variabel / static variabel
    jumlah = 0
    
    def __init__(self, inama, idarah, iattack, imovement):
        # instance variabel
        self.name = inama
        self.health = idarah
        self.attack = iattack
        self.movement = imovement
        hero.jumlah += 1
        print("membuat hero dengan nama" + inama)

hero_fanny = hero("fanny", 100, 900, 45)
print(hero.jumlah)
hero_balmond = hero("balmond", 199, 30, 39)
print(hero.jumlah)
hero_franco = hero("franco", 300, 78, 90)
print(hero.jumlah)
hero_zilong = hero("zilong", 90, 40, 24)
print(hero.jumlah)

'''
print(hero_fanny.__dict__)
print(hero.jumlah)
print(hero_balmond.__dict__)
print(hero.jumlah)
print(hero_zilong.__dict__)
print(hero.jumlah)
print(hero_franco.__dict__)
print(hero.jumlah)
'''
