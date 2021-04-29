class Hero:

    def __init__(self, name, health, attackpower):
        self.__name = name
        self.__health = health
        self.__attackpower = attackpower
    
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health
    
    def getAttackP(self):
        return self.__attackpower

    # setter

    def diserang(self, damageLawan):
        self.__health -= damageLawan
    
    def setA(self, attack_baru):
        self.__attackpower = attack_baru

# awal dari permainan
lancelot = Hero('lancelot', 200, 1000)

print(lancelot.__dict__)

# game berjalan
print(lancelot.getName())
print(lancelot.getHealth())
print(lancelot.getAttackP())
lancelot.setA(1200)
print(lancelot.getAttackP())
lancelot.diserang(500)
print(lancelot.getHealth())

if lancelot.getHealth() < 0:
    print('game over') 

