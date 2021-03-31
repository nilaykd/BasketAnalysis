#%%
import numpy as np
import pandas as pd
import functools

df2=pd.read_csv("C:/Users/ndoshi/Documents/Projects/apriori/data5.csv", encoding = "UTF-16", sep='\t', header=0)
df2.index.name="ID"

df4=df2.pivot(index='ID', columns='Recipe Name', values='Recipe Name')

def defragment(x):
    values = x.dropna().values
    return pd.Series(values, index=df.columns[:len(values)])


long_index = pd.MultiIndex.from_product([df.index, df.columns])

df3=df.stack().groupby(level='ID').apply(defragment).reindex(long_index).unstack()


df1=df.to_csv(sep=",",header=False,index=False,na_rep='')
# %%
