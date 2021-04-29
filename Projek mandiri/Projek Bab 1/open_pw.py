import sys

def manage_account():
	request_account = 'account '+sys.argv[1].replace('#','')

	if request_account.replace('account ','') == '-h':
		print('ketik seperti #<user_account/email/other>')
		sys.exit()
	file_pw = open('pw.txt','r') 
	BIG_DATA = [str(data).strip() for data in file_pw]

	DataBase = {
		user_account.replace('#','') : {user.replace('username','') : pas.replace('password','')} for (
									user_account,
									user,
									pas) in zip(BIG_DATA[::3],
												BIG_DATA[1::3],
												BIG_DATA[2::3])
	}
	print('user dan password untuk {} : \nusername : {} \npassword : {}'.format(
		request_account,
		''.join(DataBase[request_account].keys()),
		''.join(DataBase[request_account].values())))
	file_pw.close()
if __name__ == '__main__':
	manage_account()









