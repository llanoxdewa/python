class Hero:

    def __init__(self, name, darah):
        self.name = name
        self.darah = darah

    
    def showInfo(self, tipe):
        print('show info di class Hero')
        print('{} dengan darah : {}'.format(
            self.name, 
            self.darah
            )
        )

class Hero_support(Hero):
    
    def __init__(self, name):
        super().__init__(name, 200)

    def showInfo(self):
        super().showInfo('support')
    
    # override
    def showInfo(self,):
        print('showinfo di subclass Hero_support')
        print('{} \n\ttipe : support \n\tdarah : {}\n'.format(
            self.name, 
            self.darah
            )
        )



class Hero_assasin(Hero):
    
    def __init__(self, name):
        super().__init__(name, 300)
    
    def showInfo(self):
        super().showInfo('assasin')

selena = Hero_support('selena')
fanny = Hero_assasin('fanny')

selena.showInfo()
fanny.showInfo()
