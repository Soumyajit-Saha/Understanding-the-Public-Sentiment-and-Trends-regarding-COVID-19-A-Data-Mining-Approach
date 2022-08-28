# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:24:46 2022

@author: Soumyajit Saha
"""


import twint

c = twint.Config()

c.Search = ['Taylor Swift']       # topic
c.Limit = 500      # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Output = "taylor_swift_tweets.csv"     # path to csv file

twint.run.Search(c)

import pandas as pd
df = pd.read_csv('taylor_swift_tweets.csv')

print(df)