sumber = 'aieo'
tujuan = '4130'
string_input = 'kota cirebon'
tabel_traslation = str.maketrans(sumber,tujuan)
string_output = string_input.translate(tabel_traslation)
print(string_output)
# def vokal(x):
# 	for i in x:
# 		if i == 'a':
# 			return 4
# 		if i == 'i':
# 			return 1
# 		if i == 'e':
# 			return 3
# 		if i == 'o':
# 			return 0
# 		if i == ' ':
# 			break
# 	else:
# 		return i
# kata = ''.join(str(list(map(vokal,string_input))))
# print(kata)
# traslasi = {
# 	'a':'4',
# 	'i':'1',
# 	'e':'3',
# 	'o':'0'
# }
# for i in string_input:
# 	val = traslasi.get(i)
# 	string_output += val if val else i
# print(string_output)
