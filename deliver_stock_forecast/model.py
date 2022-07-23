
# coding: utf-8

# In[1]:


import pandas as pd
import datetime


# In[2]:


#dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
product_name='pen'
purchase_units=100
purchase_price=4
total_purchase=400
sales_units=75
sales_price=5
total_sales=375
profit=75


# In[3]:


dataset=pd.read_excel("dataset.xlsx",parse_dates=['date'])
dataset=dataset.iloc[:,1:]
dataset.set_index('date',inplace=True)
dataset.sort_values(by='date',inplace=True)
dataset.reset_index(inplace=True)
# dataset


# In[4]:


dataset['date'].unique()


# In[5]:


data=dataset.groupby('product name').get_group(product_name)
data=data.iloc[:,[2,3,4,5,6,7,8,9]].reset_index().iloc[:,1:]
# data


# In[6]:


x=data.iloc[:,[0,1,2,3,4,5,6]]
# x


# In[7]:


from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(7)
x=poly.fit_transform(x)
# x


# In[8]:


y=data.iloc[:,[7]]
# y


# In[9]:


#from sklearn.model_selection import train_test_split


# In[10]:


#x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


# In[11]:


from sklearn.linear_model import LinearRegression


# In[12]:


model=LinearRegression()
model.fit(x,y)


# In[13]:


y_pred=model.predict(x)


# In[14]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import math


# In[15]:


mae=mean_absolute_error(y,y_pred)
rmse=math.sqrt(mae)
r2score=r2_score(y,y_pred)


# In[16]:


print("mean squared error:",mae)
print("Root mean squared error:",rmse)
print("R2 Score:",r2score)


# In[17]:


y_pred


# In[18]:


y


# In[19]:


test=pd.DataFrame({'purchase(units)':[purchase_units],
                   'purchase price':[purchase_price],
                   'total (purchase)':[total_purchase],
                   'sales(units)':[sales_units],
                   'sales price':[sales_price],
                   'total(sales)':[total_sales],
                   'profit':[profit],})
print(test)


# In[20]:


data.iloc[0:1,:]


# In[21]:


test=poly.transform(test)



# In[22]:
print(test)

pred=model.predict(test)


# In[23]:


print("output:",int(pred[0][0]))


# %%
import pickle

pickle.dump(model, open("model.sav", 'wb'))
# %%
