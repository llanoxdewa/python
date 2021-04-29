class Hero:

    def __init__(self, name, darah, power):
        self.name = name
        self.darah = darah
        self.power = power
        self.showInfo()
    
    def showInfo(self):
        print('{} memiliki darah : {} dan power : {}'.format(self.name, self.darah, self.power))


class Hero_assasin(Hero):
    def __init__(self, name):
        super().__init__(name, 700, 900)

class Hero_tank(Hero):
    def __init__(self, name):
        super().__init__(name, 1500, 400)

class Hero_support(Hero):
    def __init__(self, name):
        super().__init__(name, 100, 300)

lancelot = Hero_assasin('lancelot')
atlas = Hero_tank('atlas')
selena = Hero_support('selena')