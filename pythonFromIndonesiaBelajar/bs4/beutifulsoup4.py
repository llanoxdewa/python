from bs4 import BeautifulSoup
import requests
import csv

with open('web/index.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')
	

### pilihan 
# -> prettify() untuk membuat parse html yang kita buat memiliki indentasion yang mirip dengan aslinya
# -> soup.<nama tag> untuk mencetak isi dari tag yang ingin kita cetak dan gunakan .text untuk mengambil textnya saja 
# soup.find('<nama tag>', class_='class name dari tag tersebut') 
# soup.find_all() untuk 
# tag['attribute'] untuk melihat/mencetak nilai atribut yang ada pada sebuah tag

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
	
	headline = article.h2.a.text
	print(f'headline :  {headline}')

	summary = article.find('div',class_='entry-content').p.text
	print(f'summary : {summary}')
		
	try:	
		vid_src = article.find('iframe',class_="youtube-player")['src']
		vid_id = vid_src.split('/')[4].split('?')[0]
		yt_link = f"https://youtube.com/watch?v={vid_id}"
	except Exception as err:
		yt_link = None	
	
	print(f'youtube link: {yt_link}','\n')







