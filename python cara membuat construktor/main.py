class hero :
    
    def __init__(self, inama, idarah, iattack, imovement):
        self.name = inama
        self.health = idarah
        self.attack = iattack
        self.movement = imovement

hero_fanny = hero("fanny", 100, 900, 45)
hero_balmond = hero("balmond", 199, 30, 39)
hero_franco = hero("franco", 300, 78, 90)
hero_zilong = hero("zilong", 90, 40, 24)
print(hero_fanny.__dict__)
print(hero_balmond.__dict__)
print(hero_zilong.__dict__)
print(hero_franco.__dict__)