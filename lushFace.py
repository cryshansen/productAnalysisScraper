#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:10:46 2020

@author: crystalhansen
"""
from lxml import html
import requests

from bs4 import BeautifulSoup
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S") 

def logInfo( action,link ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "humblebee/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 

websiteBaseUrl = "https://www.lush.ca"

lushUrl="https://www.lush.ca/en/face/face/"
#has best sellers
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/face/faceBestSellers.txt"
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
        fileName2= "lush/face/"+lushSoupItem.title.string + ".txt"
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
        #get top information section single item page elements
        for item in lushSoupItem.find_all('div', class_="product-detail"):
            #print(item.text.strip())
            f2.write(item.text.strip())
        #get item details of single page elements    
        for itemDetails in lushSoupItem.find_all('div',class_="tab-content"):
            #print(itemDetails.text.strip()) 
            f2.write(itemDetails.text.strip())
        f2.close()
        #multiple purchase items with more than one element and ingredient list
        #top level is same product-detail 
        #same tab-content
        
        
        #hit new page look for:
        #find_all('div'class_="product-ingredients-list")
        #find all('div',class_="product-ingredients"
f.close()