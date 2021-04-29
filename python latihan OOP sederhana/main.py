class Hero:

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)
    
    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        damage_diterima = attackPower_lawan//self.armor
        print('damage diterima : ' + str(damage_diterima))
        self.health -= damage_diterima
        print('sisa darah ' + self.name +' '+ str(self.health))

fanny = Hero('fanny', 200, 400, 90)
lancelot = Hero('lancelot', 198, 300, 80)
hayabusa = Hero('hayabusa', 188, 400, 40)

fanny.serang(lancelot)
print('\n')
lancelot.serang(fanny)
print('\n')
hayabusa.serang(lancelot)
print('\n')
fanny.serang(hayabusa)
print('\n')
lancelot.serang(hayabusa)

