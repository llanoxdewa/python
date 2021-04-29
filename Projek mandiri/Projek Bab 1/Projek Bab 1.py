import sys
#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {
'email': 'llanoxdewa@gmail.com',
'blog': 'https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F1%2Fc%2FMTIyMDU0MDc4NTg5&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F1%2Fc%2FMTIyMDU0MDc4NTg5&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
'luggage': '12345'}

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)
