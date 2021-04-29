
# fungsi describsi pesan
def describe(encrypt_text):
	text = ''.join([chr(int(i)) for i in encrypt_text.split('.')])
	print('<----pesan telah di descripsi---->')
	print(text)

# proses mengencrypsi pesan
massage_not_encrypt = str(input('write your mesagge >> '))
mesaage_encyrpt = '.'.join([str(ord(i)) for i in massage_not_encrypt])
print('<----pesan anda telah di encrysi---->')
print(mesaage_encyrpt)

# proses describsi pesan
if input('\napakah pesan anda ingin di descripsi ? >> ') == 'yes':
	print(describe(input()))
