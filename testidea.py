from bs4 import BeautifulSoup
import urllib.request
import re # dk what this is && scared of removing it
import time
import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

# test
url_list = [] # contains the urls in string form of all the short screener webpages
links_with_text = [] # contains the names of anything containing href in the webpage

base_url = "https://finviz.com/screener.ashx?v=111&f=sh_short_o20" # links to the finviz screener with all the short float above 20% stocks

for i in range(1, 261, 20):
    if i == 1:
        url_list.append(base_url)
    else:
        url_list.append(base_url + "&r=" + str(i))
    # moving to the next page in the short screener means adding &r=21 then &r=41 then &r=61 to the end of the url (still in string form though right now)



for url_string in url_list:
    page = urllib.request.urlopen(url_string)
    try:
        page = urllib.request.urlopen(url_string)
    except:
        print("An error occured.") 

    soup = BeautifulSoup(page, 'html.parser')

    for a in soup.find_all('a', href=True):
        if a.text:
            links_with_text.append(a['href'])



def getTheStockName(quote_url_string):
    stock_name =""
    for y in quote_url_string:
        if y.isupper():
            stock_name += y
    return stock_name

def actualSetConstructor():
    stock_set = {'AAPL'} 
    for x in links_with_text:
        if x[0] == 'q' and x[10] == '?':  
            stock_name = getTheStockName(x)
            stock_set.add(stock_name)
    return stock_set

def chartPicQuoteConstructor(stock_set): # CREATES A LIST OF THE CHARTPIC LINKS FOR EACH STOCK
    stock_link_list = []
    for i in stock_set:
        chart_pic_link = 'https://finviz.com/chart.ashx?t=' + i + '&ty=c&ta=1&p=d&s=l'
        stock_link_list.append(chart_pic_link)
    return stock_link_list
stock_link_list = chartPicQuoteConstructor(actualSetConstructor())

def getImageForDisplay(link): # this is an image that can be displayed in a tkinter Label
    img_url = link
    response = requests.get(img_url)
    img_data = response.content
    prepro1_img = Image.open(BytesIO(img_data))
    prepro2_img = prepro1_img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(prepro2_img)
    return img

root = tk.Tk()
counter =0
packing_x = 0
packing_y = 0


print(stock_link_list)
# use this in testin.py. This is a list all the links to the chart pics for different stocks.
img_list = []

'''
