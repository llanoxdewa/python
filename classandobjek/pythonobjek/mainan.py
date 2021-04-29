class Hero:
    nama = 'hero tanpa nama'
    def copy(self):
        herobaru = Hero()
        herobaru.nama = 'khaled'
        return herobaru



fanny = Hero()
fanny.nama = 'fanny'
khaled = fanny.copy()
print(fanny.nama)
print(khaled.nama)
