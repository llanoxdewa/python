## CARA YANG KURANG PYTHONIC 
# y = x.strip()
# y = y.upper()
# print(f'y upper() and strip() : {y}')
# y = y.lower()
# print(f'y lower() : {y}')
# y = y.replace(':','=')
# print(f'y replace(:,=) : {y}')
x = "	bahasa pemograman python : guido van roSSum		"
print(f'x normal : {x}')
y = x.strip().upper().replace(':',' == ')
print(f'y : {y}')