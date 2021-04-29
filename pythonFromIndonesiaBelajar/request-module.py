
import requests

# referensi {https://realpython.com/python-requests/}

## code status code pada html
# referensi (https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
# -> 2xx/succesful = ok (donwload berjalan dengan lancar)
# -> 1xx/information respone  = the request was received, continuing process
# -> 3xx/redirection =  further action needs to be taken in order to complete the request
# -> 4xx client error = the request contains bad syntax or cannot be fulfilled
# -> 5xx server error = the server failed to fulfil an apparently valid request

#hasil  = requests.get("https://xkcd.com/353/")
#print(hasil.text)

# mendownload file berektensi png dengan module request
# hasil_image = requests.get("https://xkcd.com/comics/python.png")
# with open('comic.png','wb') as file:
#	file.write(hasil_image.content)

## pilihan 
#-> status_code = untuk mengetahui status paket yang didownload
#-> text = untuk melihat struktur html paket tersebut
#-> headers = untuk menampilkan headers paket yang kita download
#-> content = untuk melihat isi content pada suatu file yang kita download
#-> json() = untuk mengebalikan data dalam bentuk dict
#head = hasil_image.headers # contoh penggunaan headers
#for k,v in head.items():
#	print(f'{k} : {v}')

### http error ###
#from requests.exceptions import HTTPError
#for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#	try:	
#		respone = requests.get(url)
#		respone.raise_for_status()
#	except HTTPError as err:
#		print(f"url {url} was not valid url")
#		print(f"error : {err}")
#	except Exception as err:
#		print(f"error : err")
#	else:
#		print('succes ful')


#respon = requests.get('https://httpbin.org/get?page2&count=25')
#menggunakan params
#payload = {'page':2,'count':25}
#respon = respon = requests.get('https://httpbin.org/get',params=payload) 
#print(respon.url)

# pilihan http method yang ada 
# requests.post('https://httpbin.org/post', data={'key':'value'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')

#payload = {'username':'ujang','password':'ujang123'}
#respon = requests.post('https://httpbin.org/post',data=payload)
#json_respon = respon.json()
#print(json_respon['form'])

# auth
#username,password = input('masukan username : '),input('masukan password : ')
#respon = requests.get(f'https://httpbin.org/basic-auth/{username}/{password}',auth=(username,password))
#
#if respon.json()["authenticated"]:
#	print('login berhasil')
#else:
#	print(f'{username} tidak valid atau {password} tidak valid')


# delay and timeout

respon = requests.get('https://httpbin.org/delay/4',timeout=3)
print(respon.text)












