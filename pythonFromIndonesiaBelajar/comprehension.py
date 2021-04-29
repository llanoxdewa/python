####################   list comprehension   ####################
# listku = [i for i in range(1,51)]
# print(listku)

## list comprehension dengan conditional if
listGrade = ['a','b','c','d','e','f']
def confersi(x):
    for i in x:
        if x == 'a':
            return 100
        if x == 'b':
            return 90
        if x == 'c':
            return 80
        if x == 'd':
            return 70
        if x == 'e':
            return 60
        if x == 'f':
            return 50
            
    
        


listNilai = list(map(confersi,listGrade))
print(listNilai)