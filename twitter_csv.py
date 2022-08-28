# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:26:35 2022

@author: Soumyajit Saha
"""

import pandas as pd
import re
# re.split('; |, ',str)

file = open('./twitter_txt/pandemic.txt','r', encoding="utf8")

text = file.read()

# print(text)

text = text.split('\n')

text = list(filter(('').__ne__, text))

df = pd.DataFrame(columns=['username', 'handle', 'postdate', 'text', 'emojis', 'reply_cnt', 'retweet_cnt', 'like_cnt'])

for t in text:
    t = t[2:-2]
    t1 = re.split("\', \'|\', \"|\", \'", t)
    df_length = len(df)
    df.loc[df_length] = t1
    # print(t1)
    
df.to_csv('./twitter_csv/pandemic.csv', index=None)
    
