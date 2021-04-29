#### python OOP ####
# a = 17 (a = identifier / 17 objek)

class Manusia:
    nama = 'no name'
    def copy(self):
        manusiaBaru = Manusia()
        manusiaBaru.nama = self.nama + " copy"
        return manusiaBaru
m = Manusia()
bilangan = 12
bilangan = 7
m2 = m.copy()
print(m.nama)
print(m2.nama)
print(bilangan)

