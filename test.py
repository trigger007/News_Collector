import requests
from bs4 import BeautifulSoup

urls=["https://www.thehindu.com/","https://timesofindia.indiatimes.com/","https://www.ndtv.com/","https://www.hindustantimes.com/"]
print("done")

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

br=requests.get(urls,headers=hdr)
soup=BeautifulSoup(br.text,"html.parser")
#s1=soup.find_all('a',{"class":"button-text link-page"})