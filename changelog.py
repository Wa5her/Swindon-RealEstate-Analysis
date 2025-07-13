# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 18:48:15 2023

@author: Eshwar
"""
import pandas as pd
import difflib
import csv

def compare_csv_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        rows1 = list(reader1)
        rows2 = list(reader2)

    changed_rows = []

    for row in rows1:
        if row not in rows2:
            changed_rows.append(row)

    for row in rows2:
        if row not in rows1:
            changed_rows.append(row)

    return changed_rows

#from datetime import date
#file name parsing to be done later
f1 ="2023-06-20Swindon_flats_buy.csv"
f2 ="2023-06-25Swindon_flats_buy.csv"
changed_rows = compare_csv_files(f1, f2)
print("Changed rows:")
for row in changed_rows:
    print(row)
#d1= pd.read_csv(f1,sep=',', encoding='utf-8');
#d2= pd.read_csv(f2,sep=',', encoding='utf-8');
