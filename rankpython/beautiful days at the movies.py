# beautiful days at the movie
# ini akan melakukan koding
# jika hari pada arr dibagi dengan hari terkecil dan hasilnya bilangan bulat
# makan hari tersebut merupakan beutiful day dan jika pecahan maka bukan


hari = [20,23,6]

# cara pribadi 
# def count_gday(day):
#     g_day = 0
#     for d in day:
#     	if (d - int(str(d)[::-1])) % min(day) == 0:
#     		g_day += 1
#     return g_day
# print(count_gday(hari))


## cara dari indonesia belajar cara ke-1
# def count_gday(i,j,k):
# 	g_day = 0
# 	for d in range(i,j+1):
# 		if (d - int(str(d)[::-1])) % k == 0:
# 			g_day += 1 
# 	return g_day

# print(count_gday(20,23,6))

## cara dari indonesia belajar cara ke-2
# def count_gday(i,j,k):
# 	return len([g_day for g_day in range(i,j+1) if (g_day - int(str(g_day)[::-1])) % k == 0])
# print(count_gday(20,23,6))











