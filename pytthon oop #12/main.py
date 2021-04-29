class Hero:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Hero_tank(Hero):
    pass

class Hero_support(Hero):
    pass

Fanny = Hero('fanny',100, 900)
balmond = Hero_tank('balmond',1000, 200)
selena = Hero_support('selena',800, 200)

print('nama hero : {} \n\tdarah hero : {} \n\thero power : {}\n'.format(Fanny.name, Fanny.health, Fanny.attack))
print('nama hero : {} \n\tdarah hero : {} \n\thero power : {}\n'.format(balmond.name, balmond.health, balmond.attack))
print('nama hero : {} \n\tdarah hero : {} \n\thero power : {}\n'.format(selena.name, selena.health, selena.attack))

