# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:02:58 2022

@author: Soumyajit Saha
"""


import pandas as pd

df = pd.read_csv('Training.csv')
df["LABEL"].replace({'1': 'Positive', '0': 'Neutral', '-1': 'Negative', 'negative': 'Negative', 'neutral': 'Neutral', 'positive': 'Positive'}, inplace=True)
# df.drop(df.loc[df['LABEL']=='N_A'].index, inplace=True)

df.to_csv('Training.csv',index=None)



# df['LABEL'] = df['LABEL'].map({1: 'Positive', 0: 'Neutral', -1: 'Negative', 'negative': 'Negative', 'neutral': 'Neutral', 'positive': 'Positive'})