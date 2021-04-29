# implace [pengurutan data terjadi didalam list siswa tanpa menghasilkan objek baru]
# dengan sorted
siswa = ['d','c','b','a']
print(f'sebelum pengurutan data siswa : {siswa}')
terurut = ' '.join(sorted(siswa))
print(f'sesudah pengurutan data siswa : {terurut}')

# dengan sort
print(f'sebelum pengurutan data siswa : {siswa}')
siswa.sort()
print(f'sesudah pengurutan data siswa : {siswa}')
