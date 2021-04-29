
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '....'
    2. dengan menggunakan double quote "..."
'''
data = 'dengan menggunakan single quote'
print(data)

data = "dengan menggunakan double quote"
print(data)

print('"halo apa kabar"')
print("'halo apa kabar'")

print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('hari ini hari jum\'at')
print('g\'day, isn\'t it ?')

# backslice
print("C:\\user\\Ucup")

# Tab
print('ucup \t\t\totong, jadi semakin jauh')

# backspace
print('otong \botong, jadi semakin dekat')

# newline
print('baris pertama. \nbarsi kedua.')# lf -> line feed -> unix, macos, linux
print('baris pertama. \rbaris kedua.')# cr -> carriage return -> comodore, acorn, lisp
print('baris pertama. \r\nbaris kedua.')# crlf -> carriage return line feed -> windows

#  3. string literal atau raw

# hati hati 
print('C:\new folder')# salah

# menggunakan raw
print(r'C:\new file')# benar

# multiline literal string
print("""
nama : Ucup
kelas : X.elektro.1
hobi : menonton anime dan membuat waktu
""")
# mulrile literal string dan raw
print(r"""
nama : bambang
kelas : X.kimia.1
alamat email : llanoxdewa@gmail.com/newID
""")



