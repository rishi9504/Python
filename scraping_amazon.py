#Here we are making a script for parsing the current price of the d3500 dslr camera from the amazon
#Later we will update this script to run every half hour and send a mail at specified address if the price is less than Rs.33000
#import important modules for parsing the data
import requests
from bs4 import BeautifulSoup
import smtplib


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('hrishikesh.pandey995@gmail.com','lpdnpqmkssymokna')

	subject = 'Price dell down'
	body = 'check the amazon link  https://www.amazon.in/gp/product/B07GW23M7T?pf_rd_p=63f66ec5-8654-4c00-843f-8b32d0b1d487&pf_rd_r=ER947NRXHZW6Z7F7V3AX'

	msg = f"Subject:{subject}\n\n\n{body}"

	server.sendmail(
		'hrishikesh.pandey995@gmail.com',
		'hrishikesh.pandey9955@gmail.com',
		msg
		)
	print ("msg has been sent")
	server.quit()
#specify the address of the product you want to check with the script
URL = 'https://www.amazon.in/gp/product/B07GW23M7T?pf_rd_p=63f66ec5-8654-4c00-843f-8b32d0b1d487&pf_rd_r=ER947NRXHZW6Z7F7V3AX'
#specifying the headers,you can search yours by doing a google search of "myheaders"
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
#we are requesting data from the url and headers we just specified
page = requests.get(URL, headers = headers)
#making a soup object to save the page content and the data
soup = BeautifulSoup(page.content, 'html.parser')
#inspect the page and check for the product title or the data you want to search
title = soup.find(id = "productTitle").get_text()
#i am checking for the price of the camera here by inspecting the data,you can specify the price of the element you want to search
price = soup.find(id="priceblock_ourprice").get_text()
#saving the price in a in format for checking,play with this for your project,its basic string split
converted_price = float(price[2:4] + price[5:8])
print(converted_price)

print(title.strip())

#this will give a response if the price is less than 33k 
if converted_price <33000.0:
	print ("BUY IT!!!")
	send_mail()








