class Hero:

    # private class variabel
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthstd = health
        self.__attPowerstd = attPower
        self.__armorstd = armor
        self.__level = 1
        self.__exp = 0

        self.__healthmax = self.__healthstd * self.__level
        self.__attPower = self.__attPowerstd * self.__level
        self.__armor = self.__armorstd * self.__level

        self.__health = self.__healthmax

        Hero.__jumlah += 1


    @property
    def info(self):
        return "{} : \n\tlevel {} \n\thealth = {}/{}  \n\tattack = {}  \n\tarmor {}".format(self.__name,self.__level, self.__health, self.__healthmax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp

        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100
            
            self.__healthmax = self.__healthstd * self.__level
            self.__attPower = self.__attPowerstd * self.__level
            self.__armor = self.__armorstd * self.__level

        if (self.__exp >= 200):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 200

            self.__healthmax = self.__healthstd * self.__level
            self.__attPower = self.__attPowerstd * self.__level
            self.__armor = self.__armorstd * self.__level

    
    def attack(self, musuh):
        self.gainExp = 50
        print(self.__name, ' attack ',musuh.__name)
    
    
            
khaled = Hero('khaled', 100, 40, 10)
fanny = Hero('fanny', 100, 40, 10)

while(1):
    serang = str(input('pilih Hero :'))
    lawan = str(input('pilih lawan :'))
    if serang == 'khaled' and lawan == 'fanny':
        khaled.attack(fanny)
    else:
        fanny.attack(khaled)
        
    print(khaled.info)

