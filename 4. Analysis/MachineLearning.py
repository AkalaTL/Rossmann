# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:10:58 2017

@author: Akala
"""

'''Rosseman analysis with Python'''
##load the data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

store = pd.read_csv('C:/Users/Akala/Desktop/DataPlay/Rossemann 20170913/2. Prepared Data/store.csv')
train = pd.read_csv('C:/Users/Akala/Desktop/DataPlay/Rossemann 20170913/2. Prepared Data/train.csv')
test = pd.read_csv('C:/Users/Akala/Desktop/DataPlay/Rossemann 20170913/2. Prepared Data/test.csv')

X = train.iloc[:,[1,2,4,5,6,7,8]].values
y = train.iloc[:,3].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# Date

# Create Year and Month columns
train['Year']  = train['Date'].apply(lambda x: int(str(x)[:4]))
train['Month'] = train['Date'].apply(lambda x: int(str(x)[5:7]))

test['Year']  = test['Date'].apply(lambda x: int(str(x)[:4]))
test['Month'] = test['Date'].apply(lambda x: int(str(x)[5:7]))

# Assign Date column to Date(Year-Month) instead of (Year-Month-Day)
# this column will be useful in analysis and visualization
train['Date'] = train['Date'].apply(lambda x: (str(x)[:7]))
test['Date']  = test['Date'].apply(lambda x: (str(x)[:7]))

# group by date and get average sales, and precent change
average_sales    = train.groupby('Date')["Sales"].mean()
pct_change_sales = train.groupby('Date')["Sales"].sum().pct_change()

fig, (axis1,axis2) = plt.subplots(2,1,sharex=True,figsize=(15,8))

# plot average sales over time(year-month)
ax1 = average_sales.plot(legend=True,ax=axis1,marker='o',title="Average Sales")
ax1.set_xticks(range(len(average_sales)))
ax1.set_xticklabels(average_sales.index.tolist(), rotation=90)

# plot precent change for sales over time(year-month)
ax2 = pct_change_sales.plot(legend=True,ax=axis2,marker='o',rot=90,colormap="summer",title="Sales Percent Change")
# ax2.set_xticks(range(len(pct_change_sales)))
# ax2.set_xticklabels(pct_change_sales.index.tolist(), rotation=90)