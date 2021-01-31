#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:07:55 2021

@author: crystalhansen

scrape site for best sellers and follow the link for the product and its content
captures 'best sellers' strategy and gets the ingredients to make a version of
use best sellers as learning of customers likes and test if changes over time. 

Also is granular and finds the best sellers of the subcategories that have per category type. 

use for analysis on cross-category interests. 

how often does this change?

"""


import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")
print('BestSellers full link following')


#BEST SELLERS
#swiper-wrapper swiper-wrapper
#product-tiles
#product

lushUrl="https://www.lush.ca/en/face/face/"

#has best sellers
#section-swiper
#swiper-container
#swiper-wrapper
#product-tiles  swiper-slide swiper
#product
# this has all the individual top level information get the link to get the ingredients

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/face/products/bestSellers_"+ d +".txt"
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
        fileName2= "lush/face/products/bestSeller_"+lushSoupItem.title.string + ".txt"
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



lushUrl="https://www.lush.ca/en/hair/hair/"

#has best sellers
#section-swiper
#swiper-container
#swiper-wrapper
#product-tiles  swiper-slide swiper
#product
# this has all the individual top level information get the link to get the ingredients

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/hair/products/bestSellers_"+ d +".txt"
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
        fileName2= "lush/hair/products/bestSeller_"+lushSoupItem.title.string + ".txt"
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



lushUrl="https://www.lush.ca/en/body/body/"
#has best sellers
#section-swiper
#swiper-container
#swiper-wrapper
#product-tiles  swiper-slide swiper
#product
# this has all the individual top level information get the link to get the ingredients

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/body/products/bestSellers_"+ d +".txt"
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
        fileName2= "lush/body/products/bestSeller_"+lushSoupItem.title.string + ".txt"
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
  
lushUrl="https://www.lush.ca/en/discover/bestsellers/?cgid=bestsellers&start=0&sz=28"
#all best sellers
#list of items 


response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/allBestSellers/allBestSellers_"+ d +".txt"
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
        fileName2= "lush/allBestSellers/bestSeller_"+lushSoupItem.title.string + ".txt"
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
