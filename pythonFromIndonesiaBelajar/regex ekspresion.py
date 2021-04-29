import re
## pola formal
# pola_kata = re.compile(r'(\d{3}) (\d{3})')
# true_kata = pola_kata.search('Rp. 200 000')
# print(true_kata.group())
# print(true_kata.group(1))
# print(true_kata.group(2))

## bila ingin menggunakan tanda kurung
# pola_kata = re.compile(r'(\(\d{3}\)) (\d{3})')
# true_kata = pola_kata.search('Rp. (200) 000')
# print(true_kata.group())
# print(true_kata.group(1))
# print(true_kata.group(2))

## penggunaan tanda | (akan mengambil kecocokan pada kata\kalimat pertama)
# pola_kata = re.compile(r'sapiderman|Spiderman')
# true_kata = pola_kata.search('sapiderman merupakan pahlawan dan sapiderman merupakan penjahat')
# print(true_kata.group())

## penggunaan tanda | untuk mencocokan beberapa hal 
# pola_kata = re.compile(r'Bat(copter|man|mobile)')
# true_kata = pola_kata.search(r'Batman sedang memperbaiki Batcopter nya')
# print(true_kata.group())	
# print(true_kata.group(1))

## Pencocokan Nol Atau Satu Kali Menggunakan Tanda Tanya ? (jika ada akan ditampilkan jika tidak ada maka tidak apa apa)
# bat_regex = re.compile(r'Bat(wo)?man')
# mo1 = bat_regex.search('Ada Batwoman di Gotham city')
# print(mo1)
# mo2 = bat_regex.search('Ada Batwoman di Gotham city')
# print(mo2.group())

# no_telp_regex = re.compile(r'(\d\d\d)?\d\d\d\d')
# mo1 = no_telp_regex.search('Nomor telepon saya 021 8273467')
# print(mo1.group())
# mo2 = no_telp_regex.search('Nomor telepon saya adalah 8273467')
# print(mo2.group())

## Pola Berulang Menggunakan Tanda Kurung Kurawal {}
# he_regex = re.compile(r'(He){3}')
# mo1 = he_regex.search('HeHeHe')
# print(mo1.group())
# bisa juga membuat batas min dan max
# he_regex = re.compile(r'(He){2,3}') #{2(batas min),3(batas maximum)}
# mo1 = he_regex.search('HeHeHe')
# print(mo1.group())
# untuk membuat regex menjadi non greedy 
# non_greedy_regex = re.compile(r'(He){2,5}?') # maka akan mengambil kata yang cocok pada min dahulu
# kalimat_non_greedy = non_greedy_regex.search('HeHeHeHeHe')
# print(kalimat_non_greedy.group())

## metode findall
# string = 'Rumah: 021 8237371 Kantor: 021 8237432'
# no_telp_regex = re.compile(r'\d{3} \d{7}') #tanpa grup
# mo = no_telp_regex.findall(string)
# print(mo) # akan mereturn list yang berisi semua string yang cocok
# no_telp_regex = re.compile(r'(\d{3}) (\d{7})') #dengan grup
# mo = no_telp_regex.findall(string)
# print(mo) # akan mereturn tuple yang berisi group dari string yang cocok

## kelas karakter
# sesuatu_regex = re.compile(r'\d+\s\w+')
# wadidaw = sesuatu_regex.findall('11 sepeda, 10 mobil, 9 pesawat, 8 komputer, 7 handphone')
# print(wadidaw)

## membuat karakter kelas sendiri 
# Kelas karakter [a-z] akan sesuai dengan semua huruf kecil dari a sampai z.
# Kelas karakter [a-zA-Z] akan sesuai dengan semua huruf baik besar maupun kecil.
# Kelas karakter [a-zA-Z0-9] akan sesuai dengan semua huruf dan juga digit.
# pola_kata = re.compile(r'\b[a-z]{2,5}\b') # hanya menerima kata yang terdiri dari a-z dengan panjang kalimat min 2 dan max 5
# kalimat = pola_kata.findall('dan mereka akhirnya bertemu, llano namanya')
# print(kalimat) # berisi kata yang terdiri dari a-z dan min panjang kata 2 dan max 5
"""
Kita juga bisa membuat kebalikan atau negasi dari 
kelas karakter dengan menggunakan tanda caret (^) 
setelah tanda pembuka [. Misalnya [^aiueoAIUEO]
(semua kata selain yang ada di [^aiueoAIUEO] akan benar)
"""
# konsonan_regex = re.compile(r'[^aiueoAIUEO]') 
# hasil = konsonan_regex.findall('Learning Python is VERY FUN')
# print(hasil)


## regex yg diawali dengan ^ dan diakhiri dengan $
# tanda ^ akan mengambil kata paling awal yang cocok
# beginsWithHello = re.compile(r'^Hello')
# a = beginsWithHello.search('Hello world!')
# print(a.group())
# # b = beginsWithHello.search('He said hello.')
# # print(b.group())
# setiap kata yang diakhiri dengan $ akan mengembalikan angka terakhir dari sebuah kalimat
# wholeStringIsNum = re.compile(r'^\d+$')
# print(wholeStringIsNum.search('1234567890')) # 1234567...
# print(wholeStringIsNum.search('12345xyz67890')) # None
# print(wholeStringIsNum.search('12 34567890')) # None

## The Wildcard Character (.)
# semua kata yang diawali (.) atau di akhiri dengan (.) akan cocok 
# dengan semua kata sejumlah titik yang telah ditentukan
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))

## Matching Everything with Dot-Star
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))
# digabungkan dengan ?
# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())
# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

## Matching Newlines with the Dot Character
# noNewlineRegex = re.compile('.*')
# print(noNewlineRegex.search("""Serve the public trust.\nProtect the innocent.
# \nUphold the law.""").group())
# 'Serve the public trust.'
# newlineRegex = re.compile('.*', re.DOTALL)
# print(newlineRegex.search("""Serve the public trust.\nProtect the innocent.
# \nUphold the law.""").group())


# REGEX SYMBOL AND YOU KNOW LAH
"""
• The ? matches zero or one of the preceding group.
• The * matches zero or more of the preceding group.
• The + matches one or more of the preceding group.
• The {n} matches exactly n of the preceding group.
• The {n,} matches n or more of the preceding group.
• The {,m} matches 0 to m of the preceding group.
• The {n,m} matches at least n and at most m of the preceding group.
• {n,m}? or *? or +? performs a nongreedy match of the preceding group.
• ^spam means the string must begin with spam.
• spam$ means the string must end with spam.
• The . matches any character, except newline characters.
• \d, \w, and \s match a digit, word, or space character, respectively.
• \d, \W, and \S match anything except a digit, word, or space character,
respectively.
• [abc] matches any characterser between the brackets (such as a, b, or c).
• [^abc] matches any character that isn’t between the brackets.
"""

## Case-Insensitive Matching
# menggunakan re.IGNORE/re.I
# fungsi re.I akan mencocokan kata tanpa memedulikan upercase atau lower case
# robocop = re.compile(r'robocop', re.I)
# print(robocop.search('RoboCop is part man, part machine, all cop.').group())
# print(robocop.search('ROBOCOP protects the innocent.').group())
# print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

## Substituting Strings with the sub() Method
# namesRegex = re.compile(r'<kata yang akan di sensor> \w+')
# namesRegex = re.compile(r'Agent \w+')
#<name>.sub(<sensor>,<kalimat>')
# namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# dengan menggunakan alternatif lain
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# y = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# print(y)

## Managing Complex Regexes
# untuk mengabaikan spasi dan komentar di dalam string ekspresi reguler.
# phoneRegex = re.compile(r"""(
# (\d{3}|\(\d{3}\))? 	# area code
# (\s|-|\.)? 			# separator
# \d{3} 				# first 3 digits
# (\s|-|\.) 			# separator
# \d{4} 				# last 4 digits
# (\s*(ext|x|ext.)\s*\d{2,5})? # extension
# )""", re.X/re.VERBOSE)

## Combining re.IGNORECASE, re.DOTALL ,and re.VERBOSE
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)




































