#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:27:42 2020

@author: crystalhansen
"""

from lxml import html
import requests

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S") 


def logInfo( action,link, messg ):
  print("info Logged" + link) 
  #write to log file action and links to trace
  fileName= "lush/log/" + action +"_"+d+".txt"
  f=open(fileName,"a")
  f.write(action +"\n" + link + ";\n\n")
  f.close()
  return 
def makeSubCategoryDir(path):
    try:
        os.mkdir(path)
    except OSError:
        logInfo ("createDir", lushSubCategoryURL,"Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    return
#https://www.lush.ca/en/hair/shampoo-bars/
#https://www.lush.ca/en/hair/shampoo/
#https://www.lush.ca/en/hair/conditioners/
#https://www.lush.ca/en/hair/hair-treatments/
#https://www.lush.ca/en/hair/styling/
#https://www.lush.ca/en/hair/curls-coils-and-texture/
# https://www.lush.ca/en/hair/pressed-conditioners/

#looking for product div and a href a title and follow link
##read the product page information and ingredients


websiteBaseUrl = "https://www.lush.ca"

#lushUrl="https://www.lush.ca/en/hair/hair/"
#lushFace = "https://www.lush.ca/en/face/face/"
#lushUrl ="https://www.lush.ca/en/face/face/"
lushUrl ="https://www.lush.ca/en/body/body/"
#lushUrl = "https://www.lush.ca/en/404" #recommendations div like best sellers
#has best sellers
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')

for subcats in lushSoup.find_all('div',class_="subcats"):
    #print(subcats)
    for href in subcats.find_all('a',class_="subcat-tile-link",href=True):  #subcat-tile-link
        #print(href['title'] + "  -----  " + href['href'])
        subCatTitle = href['title']
        lushSubCategoryURL = websiteBaseUrl + href['href']
        print("____________")
        print(lushSubCategoryURL)
        print(subCatTitle)
        print("____________")
       
        #follow Link
        categoryResponse= requests.get(lushSubCategoryURL)
        lushSoupCategory= BeautifulSoup(categoryResponse.text,'lxml')
        
        print("-~~~~~~~~~~~~~~~~~~~~")
        print(lushSoupCategory.title.string)
        print("-~~~~~~~~~~~~~~~~~~~~")
        
        fileName2= "lush/hair/"+subCatTitle + ".txt"
        
        print("==========================")
        print(fileName2)
        print("==========================")
        
        
        path = "lush/hair/"+subCatTitle + "/"
        #print(path)
        makeSubCategoryDir(path)

        f2=open(fileName2,"w")
        f2.write( href['title'] + "  -----  "  + lushSoupCategory.title.string + "\n")
       
        #need to capture the products record them and follow the product links for the product detail and tab-content ingredients
        for product in lushSoupCategory.find_all('div', class_="product"):
            #get top information section single item page elements
            #print(product.text.strip())
            f2.write(product.text.strip())
            for alink in product.find_all('a', class_="link",href=True):
                 productLink = alink['href']
                 productTitle = alink.text.strip()
                 
                 f2.write( productLink + "  -----  " + "\n"  + alink.text.strip() + "\n")
                 
                 lushSubCategoryURL = websiteBaseUrl + productLink
                 print("???????????????????")
                 print(lushSubCategoryURL)
                 print("???????????????????")
                 response2 = requests.get(lushSubCategoryURL)
                 lushProdSoup = BeautifulSoup(response2.text,'lxml')
                 print("//////////////////")
                 print(lushProdSoup.title.string)
                 print("//////////////////")
                 fileName3= path  +productTitle + ".txt"
                 print("<<<<<<<<<<<<<<")
                 print(fileName3)
                 print("<<<<<<<<<<<<<<")
                 f3=open(fileName3,"w")
                 f3.write(lushProdSoup.title.string + lushSubCategoryURL + "\n")
                 f3.write( productLink + "  -----  " + "\n" )
                 for item in lushProdSoup.find_all('div', class_="product-detail"):
                    #print(item.text.strip())
                    for description in item.find_all('div', class_="top-description"):
                        #print(description.text.strip())
                        f3.write(description.text.strip())
                    for price in item.find_all('span',"name-price"):
                        #print(price.text.strip())
                        f3.write(price.text.strip())
                        
                        
#                 #get item details of single page elements    
                 for itemDetails in lushProdSoup.find_all('div',class_="tab-content"):
                    #print(itemDetails) 
                    for itemDesc in itemDetails.find_all('div', class_="tab-pane" ):
                        print(itemDesc.get('id'))
                        if(itemDesc.get('id') == "tab-description" ):
                             print(itemDesc.text.strip()+ "\n\n")
                             f3.write(itemDesc.text.strip()+ "\n\n")
                        elif(itemDesc.get('id') == "tab-ingredients" ):
                             print(itemDesc.text.strip())
                             f3.write(itemDesc.text.strip()+ "\n\n")
                        elif(itemDesc.get('id') == "tab-how-to-use" ):
                            print(itemDesc.text.strip())
                            f3.write(itemDesc.text.strip()+ "\n\n")
                        
#                    f3.write(itemDetails.text.strip())
                 f3.close()
        f2.close()


#working fine
#        
#fileName = "lush/hair/hairBestSellers.txt"
#f=open(fileName,"w")
#for bestSellersContainer in lushSoup.find_all( 'div', class_="swiper-wrapper"):
#
#     print(bestSellersContainer.text.strip())
#    
#     f.write(bestSellersContainer.text.strip() + "\n")    
#     print("______________ Products _________________")
#     
#     for product in bestSellersContainer.find_all('div',class_="product-tiles"):
#         print("##################")
#         print(product.text.strip())
#         #f.write(product.text.strip()+ "\n\n")
#         for href in product.find_all('a', class_="link",href=True):
#            print(href['href']) 
#             #f.write(href['href'] + "\n\n" href['title']) 
#            link = href['href']
#    
#            lushItemURL = websiteBaseUrl + link
#            print(lushItemURL)
#           
#            #follow Link
#            itemResponse= requests.get(lushItemURL)
#            lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
#            
#            print(lushSoupItem.title.string)
#            fileName2= "lush/hair/products/"+lushSoupItem.title.string + ".txt"
#            f2=open(fileName2,"w")
#            f2.write(lushItemURL + "\n")
#            #get top information section single item page elements
#            for item in lushSoupItem.find_all('div', class_="product-detail"):
#                #print(item.text.strip())
#                f2.write(item.text.strip())
#            #get item details of single page elements    
#            for itemDetails in lushSoupItem.find_all('div',class_="tab-content"):
#                #print(itemDetails.text.strip()) 
#                f2.write(itemDetails.text.strip())
#            f2.close()
#        #multiple purchase items with more than one element and ingredient list
#        #top level is same product-detail 
#        #same tab-content
#        
#        
#        #hit new page look for:
#        #find_all('div'class_="product-ingredients-list")
#        #find all('div',class_="product-ingredients"
#f.close()


# def readResponse(baseUrl,startingUrl, fileName, element, class)
