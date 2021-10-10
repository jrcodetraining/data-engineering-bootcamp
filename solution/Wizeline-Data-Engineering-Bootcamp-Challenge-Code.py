#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv("profeco.csv")

df


# In[6]:


grouped = df.groupby("cadenaComercial").agg({
    "cadenaComercial": 'count'
})

grouped.count()


# In[18]:


products_grouped = df.groupby(['estado','producto'])[['precio']].count().reset_index()

products_sorted = products_grouped.groupby(['estado']).apply(lambda x: x.sort_values(['precio'],ascending = False)).reset_index(drop = True)

products_sorted.groupby(['estado']).head(10)


# In[17]:


groupedbystate_max = df.groupby(['cadenaComercial']).agg({
    'producto': 'count'
}).sort_values(['producto'], ascending=False)

groupedbystate_max


# In[23]:


products_monitored_grouped = df.groupby(['producto'])[['precio']].count().sort_values(['precio'], ascending=False)

products_monitored_grouped


# In[ ]:




