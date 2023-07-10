#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


path_dir = './Desktop/Python data sets/sales_Data/'
for files in os.listdir(path_dir):
    print(files)


# In[3]:


## First create the empty datas sets then 
##concat the data to create a merged data to get the assured data sets-


# In[4]:


FinalDf = pd.DataFrame()
for files in os.listdir(path_dir):
    Dataframe = pd.read_csv(path_dir+files)
    FinalDf = pd.concat([FinalDf,Dataframe],ignore_index = True)

FinalDf.to_csv("all_data.csv", index = False)


# In[5]:


FinalDf


# In[6]:


FinalDf.shape


# In[7]:


FinalDf.head(5)


# In[8]:


FinalDf = pd.read_csv("all_data.csv")


# In[9]:


FinalDf.head(5)                  ### Updated data frame after merging all 12 months data ina single frame:-


# In[10]:


## Data Cleaning:-


# In[11]:


FinalDf.isna().sum()


# In[12]:


FinalDf.duplicated()


# In[13]:


FinalDf.dropna()


# In[14]:


FinalDf.head(5)


# In[15]:


FinalDf.isna().sum()


# In[16]:


FinalDf["Months"] =FinalDf["Order Date"].str[0:2]
FinalDf.head(4)


# In[17]:


FinalDf.isna().sum()


# In[18]:


FinalDf = FinalDf.dropna(how = 'all')                       ### Taking out all of the Nan values in the combined data                                                                                                  #set is as follows:-
FinalDf


# In[19]:


FinalDf.isna().sum()                 # Desired Data we get:


# In[20]:


FinalDf = FinalDf[FinalDf["Order Date"].str[0:2] != 'Or']
FinalDf.head(5)


# In[21]:


FinalDf["Months"] =FinalDf["Order Date"].str[0:2]
FinalDf["Months"] =FinalDf["Months"].astype("int32")
FinalDf.head(7)


# In[22]:


FinalDf.isna().sum()


# # What was the best month foe sales? And how much did it earned from that month?

# In[23]:


# For this question we want to add another column in data as sales :-


# In[24]:


## Convertin to numeric type:-


# In[25]:


FinalDf['Quantity Ordered'] = pd.to_numeric(FinalDf['Quantity Ordered'])
FinalDf['Price Each'] = pd.to_numeric(FinalDf['Price Each'])


# In[26]:


FinalDf['Sales'] = FinalDf['Price Each'] * FinalDf['Quantity Ordered']
FinalDf['Sales']


# In[27]:


FinalDf.head(5)


# In[28]:


results =  FinalDf.groupby('Months').sum()


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


import matplotlib.pyplot as plt

months = range(1,13)
Plt.bar(months, results['Sales'])
plt.xticks(months)
plt.xlabel('MOnths')
plt.ylabel('USD dollars')
plt.show()


# # which city has got Highest no of sales:-

# In[ ]:


FinalDf.info()


# ## Add a city Address for the express of data:-

# In[48]:


## Apply method forsegregating the data set in the purchase orders:-

def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

FinalDf['City Adr'] = FinalDf['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ' )')
FinalDf.head(5)


# In[49]:


FinalDf.groupby('City Adr').sum()


# In[50]:


results = FinalDf.groupby('City Adr').sum()


# In[51]:


import matplotlib.pyplot as plt

cities = [City for City , df in FinalDf.groupby('City Adr')]

plt.bar(cities,results['Sales'])
plt.xticks(cities, rotation = 'vertical', size = 8)
plt.xlabel('City name')
plt.ylabel('Total no of Sales')
plt.show()


# ## What time should we display the advertisement to Maximize the likelihood of the customers buing products?

# In[52]:


FinalDf.head(5)


# In[53]:


FinalDf['Order Date'] = pd.to_datetime(FinalDf['Order Date'])


# In[54]:


FinalDf['Hour'] = FinalDf['Order Date'].dt.hour
FinalDf['Minute'] = FinalDf['Order Date'].dt.minute
FinalDf.head(5)


# In[107]:


hours = [hour for hour , df in FinalDf.groupby('Hour')]

plt.plot(hours, FinalDf.groupby(['Hour']).count(), color = 'darkblue')
plt.xticks(hours)
plt.xlabel('Hours')
plt.ylabel('Total no of Prooducts')
plt.grid()
plt.show()


# In[56]:


## From the above graph we concluded to show the advertisent between 11pM and 19(7) pm respectively.


# In[57]:


FinalDf.groupby(['Hour']).count()


# ###  What products often the most sold Products?

# In[58]:


FinalDf.head(5)


# In[68]:


df = FinalDf[FinalDf['Order ID'].duplicated(keep = False)]
df.head(25)


# In[71]:


df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))


# In[73]:


df.head(5)


# In[77]:


df = df[['Order ID','Grouped']].drop_duplicates()


# In[78]:


df.head(10)


# In[83]:


from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

print(count)



# In[87]:


for key, value  in count.most_common(10):
    print(key, value)


# ### What product sold the most? Why do you think it sold the most?

# In[94]:


FinalDf.head(5)


# In[99]:


product_group = FinalDf.groupyby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product , df in FinalDf.groupby('product_group')]
plt.bar(products, Quantity Ordered)
plt.xlabel('Quantity Ordered')
plt.ylabel('Products')
plt.ticks(products, rotation = 'vertical', size = 8)
plt.show()




# In[101]:


FinalDf.columns


# In[104]:


prices = FinalDf.groupby['Product'].mean()['Price_Each']
print(prices)


# In[ ]:




