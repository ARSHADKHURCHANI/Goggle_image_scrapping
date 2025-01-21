#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import os


# In[2]:


save_dir="images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


# In[3]:


headers={"User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWekit/537.36(KHTML,like Gecko) Chrome/58.0.3029.110 safari/537.56"}


# In[16]:


query="abdul kalam"
responce=requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")


# In[17]:


responce


# In[18]:


print(responce)


# In[19]:


Soup=BeautifulSoup(responce.content,'html.parser')


# In[20]:


Soup


# In[21]:


images_tags=Soup.find_all('img')


# In[22]:


images_tags


# In[23]:


len(images_tags)


# In[24]:


del images_tags[0]


# In[29]:


image_data_mongo=[]
for i in images_tags:
    image_url=i['src']
    image_data=requests.get(image_url).content
    mydict={"index":image_url,"image":image_data}
    image_data_mongo.append(mydict)
    with open(os.path.join(save_dir,f"{query}_{images_tags.index(i)}.jpg"),"wb") as f:
            
        f.write(image_data)



# In[ ]:





# In[ ]:





# In[ ]:




