import sys


def save_account():
	if sys.argv[1] == '-h':
		print('silahkan tulis seperti #<account> #<username> #<password>')
		sys.exit()
	else:
		print('your user and password accoutn has been saved !!')
	try:
		# deklarai user dan password user
		input_user_account = sys.argv[1].replace('#','')
		input_user_name = sys.argv[2].replace('#','')
		input_user_password = sys.argv[3].replace('#','')
	except:
		print('account tidak valid')


	# proses input user name dan password
	with open('pw.txt','a+') as pw_file:
		pw_file.write(f"""#account {input_user_account}\nusername {input_user_name}\npassword {input_user_password}\n""")

if __name__ == '__main__':
	save_account()
