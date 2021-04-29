class Hero:

    def __init__(self, name, darah, power):
        self.__name = name
        self.__darah = darah
        self.__power = power
    
    
    @property
    def info(self):
        return "name {} \n\tdarah : {}".format(self.__name, self.__darah)

    @property
    def power(self):
        pass

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @power.getter
    def power(self):
        return self.__power
    
    @name.setter
    def name(self, input):
        self.__name = input
    
    @power.setter
    def power(self, input):
        self.__power = input

    @name.deleter
    def name(self):
        self.__name = None
    
    @power.deleter
    def power(self):
        self.__power = None
    
    



fanny = Hero('fanny', 1000, 200)

print(fanny.name)
print(fanny.power)
fanny.name = 'lancelot'
print(fanny.name)
fanny.power = 400
print(fanny.power)
del fanny.name 
del fanny.power
print(fanny.name)
print(fanny.power)
