#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
import random


# In[11]:


headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})


# In[ ]:





# In[12]:


column_titles= ['Role', 'Company', 'Location', 'Stipend', 'Duration', 'Posted']


# In[13]:


df= pd.DataFrame(columns= column_titles)


# In[ ]:





# In[14]:


row=0


# In[15]:


for i in range(1,140):
    url='https://internshala.com/internships/'
    if i==1:
        page_url=url
    else:
        page_no= i
        page_url=url + f'page-{i}/'
    page= requests.get(page_url, headers=headers)
    soup= bs(page.text, 'html')
    blocks= soup.find_all('div', class_= 'internship_meta duration_meta')
    blocks_text= [ block.text.strip() for block in blocks]
    #
    job_title= soup.find_all('a', class_='job-title-href')
    company_title= soup.find_all('p', class_= 'company-name')
    location_title= soup.find_all('div', class_= 'row-1-item locations')
    stipend_range= soup.find_all('span', class_= 'stipend')
    duration_period= soup.find_all('div', class_= 'row-1-item')
    how_ago= soup.find_all('div', class_= ['status-success', 'status-info', 'status-inactive'])
    #
    roles= [ role.text.strip() for role in job_title]
    companies= [ company.text.strip() for company in company_title]
    locations= [location.text.strip() for location in location_title]
    stipends= [ stipend.text.strip() for stipend in stipend_range]
    durations= [ duration.text.strip() for duration in duration_period]
    durations= durations[2::3]
    posted= [ ago.text.strip() for ago in how_ago]
    #
    
    for r, c, l, s, d, p in zip(roles, companies, locations, stipends, durations, posted): # zip stops at shortest list automatically
        df.loc[row, 'Role'] = r
        df.loc[row, 'Company'] = c
        df.loc[row, 'Location'] = l
        df.loc[row, 'Stipend'] = s
        df.loc[row, 'Duration'] = d
        df.loc[row, 'Posted'] = p
        row += 1
    time.sleep(random.randint(1, 2))


# In[16]:


df


# In[ ]:





# save to csv

# In[17]:


df.to_csv(r"C:\Users\kulde\OneDrive\Desktop\data analytics\python\projects\raw_data.csv", index= False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





