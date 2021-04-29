##### membagikan permen kapda pada narapidana
##### seorang sipir jahat akan membagikan permen terakhir dengan rasa buurk


# kasus pertama 
begin = 1
permen = 2
prisoner = [i for i in range(1,6)]

## kasus kedua
# begin = 2
# permen = 2
# prisoner = [i for i in range(1,6)]

## kasus ketiga
# begin = 2
# permen = 19
# prisoner = [i for i in range(1,8)]
 
## kasus ke-4
# begin = 3
# permen = 7
# prisoner = [i for i in range(1,4)]

# def last_permen(permen,prisoner,begin):
# 	prisoner_korban = prisoner[begin:permen if begin <= 1 else permen+1]
# 	return prisoner_korban[0]

def last_permen(permen,prisoner,begin):
	hasil = (begin+permen-1)%len(prisoner)
	return len(prisoner) if hasil == 0 else hasil
print(last_permen(permen,prisoner,begin))













