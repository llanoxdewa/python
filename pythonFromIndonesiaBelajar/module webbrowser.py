import webbrowser,requests
# webbrowser.open('http://inventwithpython.com/')

# url = input('>> ')
# print(url)
# webbrowser.open(url)

### program membuat penulusuran google map otomatis
# def google_map():
# 	print('bisa juga copy alamat anda')
# 	addres = input('masukan alamat anda >> ')
# 	if len(addres) == 0:
# 		addres = pyperclip.paste()
# 	webbrowser.open(f'https://www.google.com/maps/place/{addres}')

# google_map()

## module requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# # untuk melihat status dari file yang kita donwload
#print(res.status_code == requests.codes.ok)
## untuk mengetahui error ketika sedang mendownload file
# res.raise_for_status()
## dikembangkan dengan try dan except
# try:
# 	res.raise_for_status()
# except Exception as err:
# 	print(f"problem found : {err}")

## mendownload file dari suatu website
# file_donwload = open("donwload.txt","wb")
# for kata in res.iter_content(100000):
# 	file_donwload.write(kata)
# file_donwload.close()  

### module beutifulsoup
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)








