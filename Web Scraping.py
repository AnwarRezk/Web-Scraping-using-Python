import requests
from bs4 import BeautifulSoup
import smtplib 
import time

#URL = input('enter url of the target item(copy & paste) : ')

URL = 'https://www.amazon.com/Samsung-A70-Infinity-U-Smartphone-International/dp/B07RWFC6NY/ref=sr_1_3?crid=350XK51HXG41X&keywords=samsung+galaxy+a70&qid=1563603327&s=gateway&sprefix=samsung+galaxy+a%2Caps%2C351&sr=8-3'
#The previous URL is to show how the idea works, you can choose the target item you wants..

#Just type on google -> my user agent ,user agent acts as a client in network protocol used to comm with a client server
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

#A function to check the desired price the client wants..
def check_price():
    desired_price = input("Enter your budget: ")
    desired_price = float(desired_price)
    page = requests.get(URL,headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')
    soup1 = BeautifulSoup(soup.prettify(), "html.parser") #Tricking amazon ;')
    #calling BeautifulSoup with prettify in soup1 to avoid getting None when finding any component in the page contents
    
    title = soup1.find(id='productTitle').get_text() #F12
    price = soup1.find(id='priceblock_ourprice').get_text()
    price_components = price.split(".")
    priceCut = float(price_components[0][1:]) #getting the real part of the price and discarding any decimal pts
    print(title.strip(),priceCut)

    if priceCut <= desired_price:
            send_email()


#A function to send an e-mail 
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587) #establish a server connection
    server.ehlo() #server identification
    server.starttls() #encrypting the data
    server.ehlo()

    sender_email = input("Enter the sender email(gmail) : ")
    sender_password = input("Enter the sender emaill password : ")
    #the sender email password has to be generated for security issues
    #check app passwords on google..
  

    receiver_email = input("Enter the receiver email : ")
    
    
    #login and setup subject and body of the mail
    #server.login('anwarrezk77@gmail.com' , 'wtituistitrtoovc') <- example 
    server.login(sender_email , sender_password)
    subject = 'Discount you dont want to miss!!'
    body = 'Check this offer : https://www.amazon.com/Samsung-A70-Infinity-U-Smartphone-International/dp/B07RWFC6NY/ref=sr_1_3?crid=350XK51HXG41X&keywords=samsung+galaxy+a70&qid=1563603327&s=gateway&sprefix=samsung+galaxy+a%2Caps%2C351&sr=8-3'
    
    message = f"Subject:{subject}\n\n{body}" #formatting into a string to be sent in correct form 
    server.sendmail(sender_email,receiver_email,message)

    print("E-mail sent successfully!") #confirmation 
    
    server.quit() #disconnecting from the server..

check_price()






