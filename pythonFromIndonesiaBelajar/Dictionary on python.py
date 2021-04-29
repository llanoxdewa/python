# mydict = {
# 	'one':1,
# 	'two':2,
# 	'three':3
# }
# del mydict['one'] # menghapus key dan value sesuai yang argumen yang diberikan
# print(mydict.keys()) # mereturn semua key yang ada pada suatu dict
# print(mydict.values()) # mereturn semua value yang ada pada suatu dict
# print(mydict.items()) # mereturn semua key dan value yang ada pada suatu dict
# print(mydict.get('one','not found')) # akan mereturn nilai dari key yang di pilih dan jika tidak ada maka akan mereturn 'not found'
# print(mydict.setdefault('four',4)) # akan mereturn nilai dari four jika ada jika tidak maka four akan ditambahkan didalam mydict dan sekaligus nilainya
# ###################################################################
# """
# mengunakan dict comprehension 
# """
# # list dengan bilangan genap kuadrat 
# mydict = {bil:bil**2 for bil in range(0,11) if bil%2==0}
# print(mydict)
# # list dengan key dan value yang menggunakan comprehension dan fungsi zip
# no_absen = [11,21,32,31,16]
# nama = ['llano','ujang','tatang','tarjo','sudo']
# no_absen_nama = {no:name for (no,name) in zip(no_absen,nama)}
# print(no_absen_nama)


############# mengunakan fungsi map dan lambda ###################
# fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
# # #Get the corresponding `celsius` values
# celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
# print(celsius)
# #Create the `celsius` dictionary
# celsius_dict = dict(zip(fahrenheit.keys(), celsius))
# print(celsius_dict)


############# mengunakan fungssi comprehension agar lebih singkat ########
# # Initialize the `fahrenheit` dictionary 
# fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
# # Get the corresponding `celsius` values and create the new dictionary
# celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
# print(celsius_dict)


############## if condition pada dict ########################
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # # Check for items greater than 2
# dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
# print(dict1_cond)
# print(dict1_cond)
## lebih dari dua if 
# dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
# print(dict1_doubleCond)


################### mengguanakan ternarry expression #############3
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# # Identify odd and even entries
# dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
# print(dict1_tripleCond)


#################### Nested Dictionary Comprehension ################3
# nested_dict = {'first':{'a':1}, 'second':{'b':2}}
# float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
# print(float_dict)

########################## menghitung jumlah item\nilai dalam suatu dictionary
# allGuests = {
# 'Alice': {'apples': 5, 'pretzels': 12},
# 'Bob': {'ham sandwiches': 3, 'apples': 2},
# 'Carol': {'cups': 3, 'apple pies': 1}
# }
# def totalBrought(guests,item): 
# 	jumlah_total = sum([ v.get(item,0) for v in guests.values()])
# 	return jumlah_total
# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))

###################### cara memanggil key dan value pada dictiorany ganda 
# dictiorany = {
# 	'llano':{'kelas':11,'jurusan':'elektro'},
# 	'ujang':{'kelas':12,'jurusan':'Las'},
# 	'tatang':{'kelas':11,'jurusan':'Kimia'}
# 
# for nama,nama_jurusan in dictiorany.items():
# 	print(f'nama : {nama}')
# 	for k,v in nama_jurusan.items():
# 		print(f'{k} : {nama_jurusan[k]}')
# 	print('\n')







