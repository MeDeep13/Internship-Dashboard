#!/usr/bin/env python
# coding: utf-8

# In[159]:


import pandas as pd


# In[160]:


df=pd.read_csv(r"C:\Users\kulde\OneDrive\Desktop\python\Internshala_150_pages.csv")


# In[ ]:





# In[161]:


df.drop_duplicates(inplace=True)


# In[162]:


# replacing stuff
df['Company']= df['Company'].str.replace('Limited', 'Ltd.')
df['Company']= df['Company'].str.replace('Private', 'Pvt.')
df['Location']= df['Location'].str.replace('Work from home', 'WFH')
#stripping stuff
df['Stipend']=df['Stipend'].str.strip('₹/monthweekIncentives+bonuslumpsum ')


# In[163]:


# making new columns
df[['lower_range', 'upper_range']]=df['Stipend'].str.split('-',n=2, expand=True)


# In[164]:


#exploding the rows due to different locations for the same role
df['Location'] = df['Location'].astype(str)
df['Location']=df['Location'].str.split(',\s*')
df= df.explode('Location').reset_index(drop=True)
df['Location']= df['Location'].str.strip("[[]'. ")


# In[165]:


df['Location']=df['Location'].str.replace('(Hybrid)','')
df['Location']=df['Location'].str.replace('  ','') # 2 space 
# ab ek aadha space bach hai to strip krdo sabko
df['Location']=df['Location'].str.strip()


# In[166]:


# after deleting rows i need to reset index
df.reset_index(drop=True)


# In[167]:


df['lower_range']=df['lower_range'].str.replace(',','')
df['upper_range']=df['upper_range'].str.replace(',','')
stipend_avg= []


# In[168]:


for i in range(len(df)):
    if df.loc[i,'lower_range'] == 'Unpaid':
        df.loc[i, 'lower_range'] = '0'
    if df.loc[i,'upper_range'] is None:
        df.loc[i,'upper_range'] = df.loc[i, 'lower_range']


# In[169]:


for x in df.index:
    if df.loc[x, 'lower_range']== 'Performance Based':
        df.drop(x, inplace=True)
    elif any(currency in str(df.loc[x, 'lower_range']) for currency in ['$', 'AED', 'SGD']):
        df.drop(x, inplace=True)


# In[170]:


df['lower_range']=df['lower_range'].astype(int)
(df['upper_range'])= df['upper_range'].astype(int)


# In[171]:


# $ aed gcd ye wali currency is a problem now


# In[ ]:





# In[172]:


df['est_stipend']= (df['lower_range']+df['upper_range'])/2


# In[173]:


df.drop(columns=['Stipend', 'lower_range', 'upper_range'], inplace=True)


# In[174]:


df['est_stipend']= (df['est_stipend']).astype(int)


# In[175]:


# gender retrive kr leta hu
Gender=[]


# In[176]:


for x in df.index:
    if 'Male' in str(df.loc[x,'Role']):
        Gender.append('Male')
    elif 'Female' in str(df.loc[x, 'Role']):
        Gender.append('Female')
    else:
        Gender.append('Any')


# In[177]:


df['Gender']= Gender


# In[178]:


for x in df.index:
    if ('Sales' or 'sales') in df.loc[x,'Role']:
        df.loc[x, 'Role']= 'Sales'
    if ('SEO' or 'seo') in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'SEO'
    if any(title in df.loc[x, 'Role'] for title in ['Video Making', 'Video Editing', 'Video', 'Videography']):
        df.loc[x, 'Role']= 'Video Making/Editing'
    if ('Marketing' or 'marketing') in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Marketing'
    if 'Social Media' in df.loc[x,'Role']:
        df.loc[x,'Role']= 'Social Media'
    if 'Public Speaking' in df.loc[x,'Role']:
        df.loc[x,'Role']= 'Public Speaking'
    if 'SME' in df.loc[x,'Role']:
        df.loc[x, 'Role']= 'SME'
    if ('HR' or 'Recruitment') in df.loc[x,'Role']:
        df.loc[x, 'Role']= 'HR'
    if 'Tele' in df.loc[x,'Role']:
        df.loc[x, 'Role']= 'Telecalling'
    if 'Counselling' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Counselling'
    if any(job in df.loc[x, 'Role'] for job in ['Backend Development', 'Front End Development', 'Full Stack Development', 'React', 'Node',
                                                'Flutter','Frontend', 'MERN', 'Javascript', 'Django']):
        df.loc[x, 'Role']= 'Web Development'
    if 'Consultant' in df.loc[x,'Role']:
        df.loc[x, 'Role']= 'Consultant'
    if 'Analy' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Analytics'
    if 'Fashion' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Fashion'
    if 'Graphic' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Graphic Design'
    if 'Public Relations' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Public Relations'
    if 'CA' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'CA'
    if any(keyword in str(df.loc[x, 'Role']) for keyword in ['AI', 'Machine', 'Data Science']):
        df.loc[x, 'Role'] = 'AI'
    if 'iOS' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'iOS Developer'
    if 'Software' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Software'
    if ('Game' or 'Unreal') in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Game Dev'
    if 'Mobile' in df.loc[x, 'Role']:
        df.loc[x,'Role']= 'Mobile Dev'
    if 'UI' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'UI/UX Design'
    if 'Python' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Python Dev'
    if 'Cloud' in df.loc[x, 'Role']:
        df.loc[x,'Role']= 'Cloud'
    if 'Data Science' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Data Science'
    if any(keyword in str(df.loc[x, 'Role']) for keyword in ['Finance', 'Stock', 'Trading']):
        df.loc[x, 'Role'] = 'Finance'
    if 'Business Development' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Business Development'
    if 'Research' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Market Research'
    if 'Photo' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Photography'
    if 'Customer' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Customer Support'
    if 'Operation' in df.loc[x,'Role']:
        df.loc[x, 'Role']= 'Operations'
    if 'Fund' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Fundraising'
    if 'Teach' in df.loc[x, 'Role']:
        df.loc[x, 'Role']= 'Teaching'


# In[ ]:





# In[179]:


#df['Role'].value_counts().head(40)


# In[180]:


# removing jobs which are less than 10 in number
role_counts= df['Role'].value_counts()
valid_roles= role_counts[ role_counts >= 4].index
df= df[ df['Role'].isin(valid_roles)]


# In[181]:


df['Role'].value_counts().head(40)


# In[182]:


df.to_csv(r"C:\Users\kulde\OneDrive\Desktop\data analytics\python\projects\clean_data.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




