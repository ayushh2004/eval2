#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[2]:


import pandas as pd
from pymongo import MongoClient


# In[6]:


df=pd.read_csv("Inpatient_Rehabilitation_Facility-General_Information_Sep2024 - Inpatient_Rehabilitation_Facility-General_Information_Sep2024.csv")
client=MongoClient("mongodb://localhost:27017/")
db=client['inpatient_db']
collection=db['impatient_stats']
collection.insert_many(df.to_dict('records'))
print(f"Total records inserted {collection.count_documents({})}")


# In[7]:


data=list(collection.find({}))
df=pd.DataFrame(data)
print(df.head(10))


# In[33]:


krange=range(85000,90000)
for k in krange:
    zip_providers=collection.find({"ZIP Code":"{k}"})
    print(zip_providers)


# In[19]:


profit=collection.count_documents({"Ownership Type":"For profit"})
print("Profit Ownership count ",profit)
nonprofit=collection.count_documents({"Ownership Type":"Non-profit"})
print("Non Profit Ownership count ",nonprofit)


# In[30]:


provider_birmingham_profit=collection.count_documents({"City/Town":"BIRMINGHAM","Ownership Type":"For profit"})
print("Providers with City BIRMINGHAM and Ownership-profit are ",provider_birmingham_profit)


# In[ ]:




