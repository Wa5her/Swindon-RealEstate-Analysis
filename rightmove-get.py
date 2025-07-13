# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:26:35 2023

@author: Eshwar
"""
from rightmove_webscraper import RightmoveData
#import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
import json

postcode_json = '[{"code":2392,"outcode":"SN1","town":"SWINDON"},{"code":2393,"outcode":"SN10","town":"DEVIZES"},{"code":2394,"outcode":"SN11","town":"CALNE"},{"code":2395,"outcode":"SN12","town":"MELKSHAM"},{"code":2396,"outcode":"SN13","town":"CORSHAM"},{"code":2397,"outcode":"SN14","town":"CHIPPENHAM"},{"code":2398,"outcode":"SN15","town":"CHIPPENHAM"},{"code":2399,"outcode":"SN16","town":"MALMESBURY"},{"code":2400,"outcode":"SN2","town":"SWINDON"},{"code":2401,"outcode":"SN25","town":"SWINDON"},{"code":2402,"outcode":"SN26","town":"SWINDON"},{"code":2403,"outcode":"SN3","town":"SWINDON"},{"code":2404,"outcode":"SN38","town":"SWINDON"},{"code":2405,"outcode":"SN4","town":"SWINDON"},{"code":2406,"outcode":"SN5","town":"SWINDON"},{"code":2407,"outcode":"SN6","town":"SWINDON"},{"code":2408,"outcode":"SN7","town":"FARINGDON"},{"code":2409,"outcode":"SN8","town":"MARLBOROUGH"},{"code":2410,"outcode":"SN9","town":"PEWSEY"},{"code":2411,"outcode":"SN99","town":"SWINDON"}]'
postcode_data =json.loads(postcode_json)
file_name = "Swindon_flats_buy.csv"
#range of post codes to collect data
outcode_min = 2392
outcode_max = 2410

#loop through each postcode and append to snb
for outcode in range(outcode_min,outcode_max+1):
    url = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=OUTCODE%5E"+str(outcode)+"&minBedrooms=3&maxPrice=1000000&minPrice=200000&propertyTypes=bungalow%2Cdetached%2Cflat%2Csemi-detached%2Cterraced&includeSSTC=false&mustHave=garden%2Cparking&dontShow=newHome%2Cretirement%2CsharedOwnership&furnishTypes=&keywords="
    sna = RightmoveData(url).get_results
    sna['PostCode'] = postcode_data[outcode-outcode_min]['outcode']
    sna['Town'] = postcode_data[outcode-outcode_min]['town']
    
    if outcode!=outcode_min:
        snb = pd.concat([snb, sna])
    else:
        snb = sna
    
#Save data to file     
snb.to_csv(str(date.today())+file_name, sep=',', encoding='utf-8')
