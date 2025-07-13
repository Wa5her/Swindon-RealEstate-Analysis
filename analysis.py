# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:55:56 2023

@author: Eshwar
"""
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
#plt.figure(dpi=1200,figsize=(16, 10)) 

#File to read 
file_name = "Swindon_flats_buy.csv"
file_name = str(date.today())+file_name
#filename = "Swindon_flats_buy2023-06-20.csv"

#Read the data
SNdata = pd.read_csv(file_name,sep=',', encoding='utf-8')

#Sort data by ppeak median 
# Calculate median values for each group
medians = SNdata.groupby('PostCode')['price'].median().sort_values()

# Create a new column for sorting the DataFrame
SNdata['Group_Order'] = SNdata['PostCode'].map(medians)

# Sort the DataFrame by the new column
SNdata = SNdata.sort_values('Group_Order')

# Create the box plot using DataFrame.boxplot()
fig, ax = plt.subplots(figsize=(16, 9))
SNdata.boxplot(column='price', by='PostCode',ax=ax)
ax.plot(ax.get_xticks(),color='red')
#SNdata.plot.scatter(x='PostCode', y='price', color='blue', ax=ax)
#ax.plot(ax.get_xticks(),color='blue')
# scatter plot is here 
ax.scatter(SNdata['PostCode'],SNdata['price'])
#SNdata.boxplot(column='price',by='PostCode',ax=ax)














# Set the plot title and axis labels
plt.title('Price vs Postcode')
plt.xlabel('PostCode')
plt.ylabel('Price')
ax.minorticks_on()
ax.grid(which='minor', axis='y', linestyle='--')
ax.grid(which='major', axis='x', linestyle='-', linewidth='0')


# Display the plot
plt.show()
