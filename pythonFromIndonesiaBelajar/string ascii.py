import string

# uper case
print(string.ascii_uppercase)
# lower case
print(string.ascii_lowercase)

############# mengunakan chr dan ord
"""
alfabet = list(chr(i) for i in range(ord('a'),ord('z')+1))

pengertian ord
{
	Fungsi ord() berfungsi untuk mengembalikan kode bilangan unicode dari sebuah karakter string. Fungsi ord() adalah kebalikan dari fungsi chr(). Fungsi ord() memiliki satu parameter, yaitu: c – string karakter yang akan dicari kode bilangan unicodenya.
}

pengertian chr
{
	Deskripsi Fungsi chr() mengembalikan karakter unicode dari bilangan integer (mengubah integer menjadi string) Sintaks Fungsi chr() memiliki sintaks seperti berikut: chr(i) Parameter i - integer, bilangan yang akan diubah jadi karakter unicode Nilai Kembalian Fungsi chr() mengembalikan karakter unicode yang bersesuaian
}
"""


