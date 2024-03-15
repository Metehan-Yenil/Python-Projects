import requests
from bs4 import BeautifulSoup
from send_email import sendMail

response=requests.get('http://api.open-notify.org/astros.json')
url1="https://www.trendyol.com/my-valice/smart-bag-strong-usb-sarj-girisli-unisex-abs-akilli-sirt-cantasi-siyah-p-649535535"

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
    }

page = requests.get(url1,headers=headers)

htmlPage= BeautifulSoup(page.content,'html.parser')

productTitle=htmlPage.find("h1" , class_= "pr-new-br").getText()

price=htmlPage.find("span",class_="prc-dsc").getText()
image = htmlPage.find("img",class_="product-image-container")
convertedPrice= float(price.replace(",",".").replace(" TL",""))

print(productTitle)


if(convertedPrice<=1000):
    print("ürünün fiyati düşmüştür.")
    htmlEmailContent="""/
    <html>
    <head>
    </head>
    <body>
    <h3>{0}</h3>
    <br/>
    {1}
    <br/>
    <p>Ürün linki: {2}</p>
    </body>
    </html>
    
    """.format(productTitle,image,url1)
    sendMail("metehanynl@gmail.com","ürünün fiyati düştü indirimli fiyat="+price,htmlEmailContent)
    print(convertedPrice)
    print("Email gönderildi")