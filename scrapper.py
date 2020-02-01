import requests
from bs4 import BeautifulSoup
from re import sub
import time
import webbrowser as wb

URL = 'https://www.amazon.de/Elements-Portable-externe-Festplatte-WDBU6Y0020BBK-WESN/dp/B06W55K9N6/ref=sr_1_17?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=ssd+extern+usb+c&qid=1580494002&sr=8-17'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}


def open_page():
    firefox = wb.get('firefox')
    firefox.open_new_tab(URL)


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    wished_price = 70.00
    title = soup.find(id="productTitle").get_text()
    #print(title.strip())
    price = soup.find(id='priceblock_ourprice').get_text()
    euro_str = '\xa0€'
    price = sub(euro_str, '', price).replace(',', '.')
    converted_price = float(price)
    print('price was checked: ', converted_price)  

    if converted_price < wished_price:
        open_page()
        

while True:
    check_price()
    time.sleep(60 * 60)
