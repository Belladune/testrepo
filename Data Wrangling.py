#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")


# In[13]:


df


# In[12]:


#find how many duplicates rows exist`
df.duplicated().sum()


# In[28]:


df.drop_duplicates(inplace=True)
df.shape


# In[29]:


df.isnull().sum()


# In[30]:


df.isnull().any(axis=1).sum()


# In[31]:


df["WorkLoc"].isnull().sum()


# In[34]:


df["WorkLoc"].value_counts()


# In[44]:


print('There are', df['WorkLoc'].nunique(), 'unique Work Locations in the survey:')

print('\nWorkLoc                                    value count')      
print('-------                                    -----------')
print(df['WorkLoc'].value_counts())

print('\n\nThere are', df['Employment'].nunique(), 'unique Employment values in the survey:')

print('\nEmployment        value count')      
print('----------        -----------')
print(df['Employment'].value_counts())

print('\n\nThere are', df['UndergradMajor'].nunique(), 'unique UndergradMajor values in the survey:')

print('\nUndergradMajor        value count')      
print('---------------        -----------')
print(df['UndergradMajor'].value_counts())


# In[36]:


df["Dependents"].value_counts()


# In[68]:


df["Respondent"]


# In[47]:


# your code goes here
import numpy as np

workloc_highest = 'Office'

missing_data = df.isnull()
#print(missing_data.head(5))

print('\nValue counts for missing data in WorkLoc:\n')
print( missing_data['WorkLoc'].value_counts())


print('\nHere are the first 10 rows missing values for WorkLoc:')
print(df[missing_data['WorkLoc']][['Respondent','WorkLoc']].head(10))

df['WorkLoc'].replace(np.nan, workloc_highest, inplace=True)


# In[49]:


df["WorkLoc"].isnull().sum()


# In[51]:


df["CompFreq"].isnull()


# In[52]:


df.loc[df['CompFreq'] == 'Yearly', 'NormalizedAnnualCompensation']  = 1  * df['CompTotal']
df.loc[df['CompFreq'] == 'Monthly', 'NormalizedAnnualCompensation'] = 12 * df['CompTotal']
df.loc[df['CompFreq'] == 'Weekly', 'NormalizedAnnualCompensation']  = 52 * df['CompTotal']


df[['CompTotal','CompFreq','NormalizedAnnualCompensation']].head(20)

df['NormalizedAnnualCompensation'].median()


# In[73]:


df["EdLevel"].isnull().sum()


# In[74]:


df["CompFreq"].nunique()


# In[75]:


df["CompFreq"].value_counts()


# In[ ]:




