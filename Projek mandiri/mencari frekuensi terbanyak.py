data_pendapatan = {
	'januari':None,
	'februari':None,
	'Maret':None,
	'april':None,
	'Mei':None,
}

for bulan in data_pendapatan:
	data_pendapatan[bulan] = int(input(f'masukan pendapatan pada bulan {bulan} >> '))
#max_pendatapan = [bulan for bulan in data_pendapatan if data_pendapatan[bulan] == max(data_pendapatan.values())]
max_pendatapan = max(data_pendapatan.values())
for bulan in data_pendapatan:
	if data_pendapatan[bulan] == max_pendatapan:
		max_pendatapan = bulan
print('pendapatan terbanyak terjadi di bulan {}'.format(max_pendatapan))
	

