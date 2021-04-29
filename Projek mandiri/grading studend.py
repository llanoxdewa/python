Grade = [73,67,38,33]


def cgrade(grade):
	for i, g in enumerate(grade):
		if g == 38:
			g += 2
			grade[i] = g
		elif g > 40 and (g + 1) % 5 == 0:
			g += 1
			grade[i] = g
		elif g > 40 and (g + 2) % 5 == 0:
			g += 2
			grade[i] = g
	return grade 
print(Grade)
print(cgrade(Grade))


