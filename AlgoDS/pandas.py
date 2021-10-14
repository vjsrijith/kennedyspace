# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:05:36 2021

@author: 212709023
"""


import pandas as pd

df=pd.read_csv('C:\\Users\\212709023\\Desktop\\Udemy\\Python\\medic.csv')
# print(df.loc[2])
# for row in df.index:
#     if df.loc[row]['Duration'] ==45:
#         print(df.loc[row])



data = { 'id':[1,2,3,4,5,4],
        'date':['2020-10-10','2020-10-10','2020-10-10','2020-10-10','2020-10-10','2020-10-11']
        }


df1=pd.DataFrame(data)
df1.drop_duplicates('id',inplace=True)
# df2=df1.dropna()
print(df1)

print(df1.dtypes)
# df1['date'].fillna('2020-01-01',inplace=True)
# df1['id'].fillna(0,inplace=True)


# df1['date_conv']=pd.to_datetime(df1['date'])

# df1['id']=df1.id.astype('str')
# df1['id']=df1.id.astype('float')
# df1['id']=df1.id.astype('int')
