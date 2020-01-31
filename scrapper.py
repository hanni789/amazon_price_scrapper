import requests
from bs4 import BeautifulSoup
from re import sub
import smtplib
import time

URL = 'https://www.amazon.de/gp/product/B0744D858V?pf_rd_p=671e72bc-8864-4ab6-8ef7-60da5d6ead8c&pf_rd_r=XQNJZXM89HRJ4M7B7ME0'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('johklunk@gmail.com', 'lxivyrlwqxamazgl')

    subject='Price fall down!' 
    body = 'Check the amazon link:' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('johklunk@gmail.com', 'wSmo7RLZo5@web.de', msg)
    print('Email has send')
    server.quit()

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    wished_price = 35.00
    title = soup.find(id="productTitle").get_text()
    #print(title.strip())
    price = soup.find(id='priceblock_ourprice').get_text()
    euro_str = '\xa0€'
    price = sub(euro_str, '', price).replace(',', '.')
    converted_price = float(price)
    print('price for Portmonee was checked: ', converted_price)  

    if converted_price < wished_price:
        send_mail()

while True:
    check_price()
    time.sleep(60 * 60)
