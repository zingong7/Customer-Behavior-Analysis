#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("customer_shopping_behavior.csv")


# In[2]:


df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# # Data Cleaning

# In[5]:


df.isnull().sum()


# In[6]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[7]:


df.isnull().sum()


# In[8]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")


# In[9]:


df=df.rename(columns={'purchase_amount_(usd)':"purchase_amount"})


# In[10]:


df.columns


# ## Creating a column of age_group

# In[11]:


labels=['Young Adult','Adult','Middle-aged','Senior']


# In[12]:


df['age_group']=pd.qcut(df['age'],q=4,labels=labels)


# In[13]:


df[['age','age_group']].head()


# # Creating column Purchase frequency days

# In[14]:


df.frequency_of_purchases.unique()


# In[15]:


purchase_days={
    'Fortnightly':14,
    'Weekly':7,
    'Annually':365,
    "Quarterly":90,
    'Bi-Weekly':14,
    "Monthly":30,
    'Every 3 Months':90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(purchase_days)


# # Creating segmentation column based on previous purchases done by a customer

# In[16]:


def segment(x):
    if x == 1:
        return "New"
    elif x>1 and x<=5:
        return "Returning"
    elif x>5:
        return "Loyal"
df['customer_segment']=df['previous_purchases'].transform(lambda x:segment(x))


# In[17]:


df.head(5)


# In[18]:


df.drop("promo_code_used",axis=1,inplace=True)
df.drop("frequency_of_purchases",axis=1,inplace=True)


# # Performing EDA

# In[19]:


numeric_cols=df.select_dtypes(include=np.number).columns
plt.figure(figsize=(15,8))
plt.subplot(3,2,1)
plt_index=1
for i ,col in enumerate(numeric_cols):
    if col == 'customer_id':
        continue
    plt.subplot(3,2,plt_index)
    sns.histplot(x=df[col])
    plt_index+=1
plt.tight_layout()
plt.show()


# In[20]:


categorical_cols=df.select_dtypes(include=['object','category']).columns
categorical_cols
plt.figure(figsize=(15,15))
plt_catindex=1
for i, cat in enumerate(categorical_cols):
    if cat in ('item_purchased','location','color'):
        continue
    plt.subplot(4,3,plt_catindex)
    sns.countplot(data=df,x=cat)
    plt_catindex+=1
    if cat in ("shipping_type",'payment_method'):
        plt.xticks(rotation=90)
plt.tight_layout
plt.show()


# In[21]:


df.groupby(['discount_applied','age_group'])['purchase_amount'].sum().unstack().plot(kind='bar')
plt.title("Affect on discount based on age groups")
plt.xlabel("Discount Applied")
plt.ylabel("Purchase Amount")
plt.show()


# In[22]:


data=df.groupby('gender')['purchase_amount'].sum().reset_index()
sns.barplot(x="gender",y="purchase_amount",data=data)
plt.title("Sales based on gender")
plt.xlabel("")
plt.ylabel("Amount Spent on shopping")
plt.show()


# In[23]:


customer=df.groupby(['customer_segment','subscription_status'])['subscription_status'].count().sort_values().reset_index(name="count")
sns.barplot(data=customer,x='customer_segment',y='count',hue='subscription_status')
plt.title("Subscription status as per customer segment ")
plt.xlabel("")
plt.ylabel("Number of customers")
plt.legend(title='Subscription Status')
plt.tight_layout
plt.show()


# In[24]:


df2 = df.groupby(['season','category'])['purchase_amount'].sum().unstack()

ax = df2.plot(kind='bar', stacked=True, figsize=(10,6), colormap='tab20')

# Add values on each segment
for i, season in enumerate(df2.index):
    bottom = 0
    for cat in df2.columns:
        value = df2.loc[season, cat]
        ax.text(i, bottom + value/2, f"{int(value)}", ha='center', va='center', fontsize=9)
        bottom += value

plt.title("Purchase Amount by Season and Category")
plt.ylabel("Total Purchase Amount")
plt.xlabel("Season")
plt.xticks(rotation=0)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# # Connecting to postgres sql

# In[25]:


pip install psycopg2-binary sqlalchemy


# In[26]:


from sqlalchemy import create_engine
username='postgres'
password='1234'
host='localhost'
port='5432'
database='customer_behaviour'

engine=create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
table_name='customer'
df.to_sql(table_name,engine,if_exists='replace',index=False)

print(f"Data sucessfully loaded into table {table_name} in database {database}.")

