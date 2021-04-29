class hero : # template
    pass


hero1 = hero() # object / instance (instansiate)
hero2 = hero()
hero3 = hero()

hero1.nama = "balmond"
hero1.health = 200

hero2.nama = "fanny"
hero2.health = 199

hero3.nama = "franco"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.nama)