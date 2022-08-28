# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:32:57 2022

@author: Soumyajit Saha
"""


import pandasql as ps
import pandas as pd
from datetime import datetime

filename = ['US','GB','IN','DE','FR','JP','ZA','CA','EG','GH']
filename2 = ['USA','UK','India','Germany','France','Japan','South_Africa','Canada', 'Egypt','Ghana']

for f in range(len(filename)):

    df = pd.read_excel(filename[f] +  '.xlsx')
    # print(df)
    
    dates = df['date'].to_list()
    
    # dates_2 = []
    # for d in dates:
    #     dates_2.append(datetime.strptime(d, '%Y-%m-%d'))
    
    month = []
    day = []
    year = []    
    for i in dates:
        month.append(i.month)
        day.append(i.day)
        year.append(i.year)
        
    df['day'] = day
    df['month'] = month
    df['year'] = year
    
    df.columns = df.columns.str.replace(' ','_')
    df.columns = df.columns.str.replace('-','_')
    
    q1 = """
    
    SELECT month, year, SUM(covid) AS covid,	SUM(vaccine) AS vaccine,	SUM(Wuhan) AS Wuhan,	SUM(vaccination) AS vaccination,	SUM(lockdown) AS lockdown,	SUM(quarantine) AS quarantine,	SUM(sanitizer) AS sanitizer,	SUM(mask) AS mask, 	SUM(delta) AS delta, 	SUM(omicron) AS omicron,	SUM(alpha) AS alpha, 	SUM(covid_test) AS covid_test,	SUM(booster) AS booster,	SUM(social_distance) AS social_distance, 	SUM(pandemic) AS pandemic,	SUM(corona) AS corona, 	SUM(sARS_CoV_2) AS SARS_COV_2 
    FROM df
    GROUP BY month, year
    ORDER BY year
    
    """
    
    df2 = ps.sqldf(q1, locals())
    df2.to_csv('Google_' + filename2[f] + '_monthly.csv', index=None)