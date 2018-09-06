# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:49:30 2018

@author: M263855
"""

import pandas as pd

sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 50],
         'Feb': [200, 210, 90],
         'Mar': [140, 215, 95],
         'list_x':[['Iron Man','Thor','Ant-Man'],['Quicksilver','Swordsman','Black Panther'],['Doctor Strange','Quake','Nightmask']]}
df = pd.DataFrame.from_dict(sales)

#%% 1. How to query if a list-type column contains a query string?
query_str = 'Iron Man'

mask = df['list_x'].apply(lambda x: query_str in x)
df_01 = df[mask]

df_01_02 = df_01[[query_str in x for x in df_01['list_x']]]


