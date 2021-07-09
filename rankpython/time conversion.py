# PM --> dari jam 12 siang sampai jam 12 malam
# AM --> dari jam 00.01 sampai jam 12 siang

jam12 = '12:01:45AM'
def convertjam(s):
	jam = int(s[:2])
	if jam != 12 and jam >= 1  and s[-2:] == 'PM':
		jam += 12
	elif jam == 12 and s[-2:] == 'AM':
		jam = 0
	return '{j:02d}{md}'.format(j=jam,md=s[2:-2])

print(f'jam dalam format 12jam : {jam12}')
print(f'jam dalam format 24jam : {convertjam(jam12)}')
