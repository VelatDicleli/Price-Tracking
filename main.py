import requests
from bs4 import BeautifulSoup
import time
import smtplib


url = "https://www.trendyol.com/ronic-nutrition/whey-ultimate-4000-g-kas-yapilanmasina-yardimci-protein-tozu-cikolata-aromali-p-32867763"

headers = {"User-Agent":
               " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

def PriceChecker():
  page = requests.get(url, params=headers)

  hPage = BeautifulSoup(page.content, 'html.parser')

  ProductName = hPage.find("h1", class_="pr-new-br").get_text()

  price=hPage.find("span", class_="prc-dsc").get_text()

  Price=float(price.replace("TL","").replace(",","."))


  if(Price<1050):
    mailSender()
  else:
      print("fiyat düsmedi")



def mailSender():
    sender = "velatdicleli@gmail.com"
    receiver = "diclelivelat@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login(sender, "ruwrrboqxasvbqgp")

    message= "fiyat dustu simdi urunu alabilirsin"
    link="su linke tikla... " + url
    mailcontent=f' alici={receiver} \n gonderen={sender}\n\n\n  ISTE SANA FIRSAT!! ={message} {link}'
    server.sendmail(sender,receiver,mailcontent)
    print("mail gonderildi")
    server.quit()




while(1):
    PriceChecker()
    time.sleep(1)





