
import shelve,sys,pyperclip
try:
	command = sys.argv[1]
	name = sys.argv[2]
except:
	print('command not found')

def save_file():
	data_save = shelve.open('data-saving')
	data_save[name] = pyperclip.paste()
	print('your data has been saving')
	data_save.close()
def open_file():
	data_open = shelve.open('data-saving')
	print(data_open[name])
	data_open.close()
def delete_file():
	delete_data = shelve.open('data-saving')
	del delete_data[name]
	print('data has been delete from your data-saving')

if len(sys.argv)==3 and sys.argv[1].lower() == 'save':
	save_file()
elif len(sys.argv)==3 and sys.argv[1].lower() == 'open':
	open_file()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	delete_file()
else:print('command not found')






















