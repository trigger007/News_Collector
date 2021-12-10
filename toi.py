import requests
from bs4 import BeautifulSoup

url="https://timesofindia.indiatimes.com/"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
print("Choose the category")
cat="city,india,world,business,tech,sports,tv/english,etimes,web-series/reviews"
cat=cat.split(",")
print(cat)
br=requests.get(url,headers=hdr)
soup=BeautifulSoup(br.text,"html.parser")

url1="https://timesofindia.indiatimes.com/city/kolkata"
br=requests.get(url1,headers=hdr)
soup=BeautifulSoup(br.text,"html.parser")
s=soup.find_all('div',{"class":"_2ZXWE"})

aws=s[0].find_all('a')
for i in aws:
    print(i.text)







