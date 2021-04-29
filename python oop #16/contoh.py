
class Role_hero:
    
    def roleHero(self,role):
        self.role = role
    
    def showRole(self):
        print('Role hero :',self.role)

class Team_hero:
    
    def teamHero(self,team):
        self.team = team

    def showTeam(self):
        print('Team :',self.team,'\n')

class Hero(Team_hero,Role_hero):
    
    def __init__(self,name,darah):
        self.name = name
        self.darah = darah
    
    def showAll(self):
        print(self.name)
        super().showRole()
        super().showTeam()

fanny = Hero('fanny',900)
fanny.roleHero('assasin')
fanny.teamHero('kawan')
fanny.showAll()

balmond = Hero('balmond',1200)
balmond.roleHero('tank')
balmond.teamHero('lawan')
balmond.showAll()

