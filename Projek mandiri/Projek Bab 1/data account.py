import sys
from save_pw import save_account as SA
from open_pw import manage_account as MC

print('-----------------------------WELCOME--------------------------')

try:
	choice = sys.argv[-1]
	if choice == '-N':
		SA()
	elif choice == '-O':
		MC()
	elif choice == '-h':
		print("""
-h -N (membuka petuntuk untuk menyimpan ducoment baru)

-h -O (membuka petuntuk untuk membuka ducoment yang sudah tersimpan)
	
#<argumen> #<argumen> #<argumen> -O (membuat document baru )
	
#<argumen> -O (membuka document yang tersimpan )
			""")	
	elif choice == choice[0]:print('input tidak valid\nketik python data account -h untuk informasi lebih lanjut')
except:
	print('<-h>')


