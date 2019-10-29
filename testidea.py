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
        print("An error occured.") # TODO THERE MIGHT BE AN ERROR WHERE THERE ISN'T UP TILL A PAGE https://finviz.com/screener.ashx?v=111&f=sh_short_o20&r=241

    soup = BeautifulSoup(page, 'html.parser')

    for a in soup.find_all('a', href=True):
        if a.text:
            links_with_text.append(a['href'])


# todo NOW just load up the names of the stocks
def getTheStockName(quote_url_string):
    # just find all the capital letters lol
    # the stock name till be the only one in capital letters, rest of the quote url string will nah be
    stock_name =""
    for y in quote_url_string:
        if y.isupper():
            stock_name += y
    return stock_name

def actualSetConstructor():
    stock_set = {'AAPL'}  # set to prevent duplicate elements from being added in. I made it a stock name lol so that I don't get an error down a few lines I put merge this with https://finviz.com/ so if I put something random beautifulsoup can't google it then error
    for x in links_with_text:
        if x[0] == 'q' and x[10] == '?':  # checking if 'quote.ashx?t=' is present in the line
            stock_name = getTheStockName(x)
            stock_set.add(stock_name)
    return stock_set

def chartPicQuoteConstructor(stock_set): # CREATES A LIST OF THE CHARTPIC LINKS FOR EACH STOCK
    # you want https://finviz.com/chart.ashx?t=TROV&ty=c&ta=1&p=d&s=l
    stock_link_list = []
    for i in stock_set:
        chart_pic_link = 'https://finviz.com/chart.ashx?t=' + i + '&ty=c&ta=1&p=d&s=l'
        stock_link_list.append(chart_pic_link)
    return stock_link_list
stock_link_list = chartPicQuoteConstructor(actualSetConstructor())
# just get the fucking set of all the stock names printed you dunbunct

'''alternatively just construct the stupid chart quote with the name of the stock also can la FUCK 

all I need is the name of the stock. That one can borrow the func from the java version of this that I wrote 20 years ago. 
'''
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
for i in range(len(TEST_stock_link_list)):
    img_list.append(getImageForDisplay(TEST_stock_link_list[i])) # the images added into each label inited need to have different titles
    # same issue as with the arrows in unity
    # if a single img variable is being changed every loop, then every label img is affected
    # which causes there to be blank labels
    if i%11 == 0:
        tk.Label(root, image=img_list[counter]).pack()
    else:
        tk.Label(root, image=img_list[counter]).pack(side = 'right')
    time.sleep(45)

# TODO remember to put the queries on a sleep timer otherwise get attacked by google/finviz
root.mainloop()

'''