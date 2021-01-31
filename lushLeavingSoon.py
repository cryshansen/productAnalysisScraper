#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:34:57 2021

@author: crystalhansen
"""


import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

print('Leaving Soon')


lushUrl="https://www.lush.ca/en/discover/leaving-soon/?cgid=leaving-soon&start=0&sz=70"



response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/leaving/leavingSoon_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = websiteBaseUrl + link
        #print(lushItemURL)
        
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        #print(lushSoupItem.title.string)
        fileName2= "lush/leaving/products/"+lushSoupItem.title.string+ "_"+d + ".txt"
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
        f2.write(link +"\n")
        #get top information section single item page elements
        for item in lushSoupItem.find_all('div', class_="product-detail"):
            #print(item.text.strip())
            f2.write(item.text.strip())
        #get item details of single page elements    
        for itemDetails in lushSoupItem.find_all('div',class_="tab-content"):
           # print(itemDetails.text.strip()) 
            f2.write(itemDetails.text.strip())
        f2.close()
        
        
f.close()