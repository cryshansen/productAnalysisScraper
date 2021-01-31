#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:10:21 2020

@author: crystalhansen
"""
from lxml import html
import requests

from bs4 import BeautifulSoup
#from datetime import datetime, timedelta
 
websiteBaseUrl = "https://www.lush.ca"


lushUrl= "https://www.lush.ca/en/discover/50-off/?cgid=boxing-day&start=0&sz=224"  

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/boxingDay/boxingDaySales.txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = websiteBaseUrl + link
        #print(lushItemURL)
        #/en/body/massage-bars/therapy/9999903865.html
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        #print(lushSoupItem.title.string)
        fileName2= "lush/boxingDay/"+lushSoupItem.title.string + ".txt"
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
       
lushUrl="https://www.lush.ca/en/bath-shower/?cgid=bath-shower&start=0&sz=226"

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/bath-shower/bath-shower.txt"
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
        fileName2= "lush/boxingDay/"+lushSoupItem.title.string + ".txt"
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
        
f.close()


lushUrl="https://www.lush.ca/en/hair/hair/"
#feed page, element, class, any other tags to grab aka a href and a title


#'div', subcat-tile
#a subcat-tile-link get ->href ->title
#follow link


#BEST SELLERS
#swiper-wrapper swiper-wrapper
#product-tiles
#product

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/hair/hair.txt"
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
        fileName2= "lush/hair/"+lushSoupItem.title.string + ".txt"
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
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

lushUrl="https://www.lush.ca/en/face/face/"
#has best sellers
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/face/face.txt"
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
#https://www.lush.ca/en/body/?cgid=all-body&start=0&sz=28
lushUrl="https://www.lush.ca/en/body/body/"
#best sellers
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/body/BodyProducts.txt"
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
        fileName2= "lush/body/"+lushSoupItem.title.string + ".txt"
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


lushUrl="https://www.lush.ca/en/gifts/?cgid=all-gifts&start=0&sz=161"
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/gifts/GiftItems.txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = websiteBaseUrl + link
        #print(lushItemURL)
        #/en/body/massage-bars/therapy/9999903865.html
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        #print(lushSoupItem.title.string)
        fileName2= "lush/gifts/"+lushSoupItem.title.string + ".txt"
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


lushUrl="https://www.lush.ca/en/all-gift-cards.html"        
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/giftCard/giftCards.txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = websiteBaseUrl + link
        #print(lushItemURL)
        #/en/body/massage-bars/therapy/9999903865.html
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        #print(lushSoupItem.title.string)
        fileName2= "lush/giftCard/"+lushSoupItem.title.string + ".txt"
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