# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:45:58 2022

@author: Soumyajit Saha
"""


import pandas as pd
from datetime import datetime
import numpy as np
import pandasql as ps

df = pd.read_csv('covid_Egypt_data.csv')
# print(df)

# df['Dates'] = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

dates = df['Dates'].to_list()

dates_2 = []
for d in dates:
    dates_2.append(datetime.strptime(d, '%b %d, %Y'))

month = []
day = []
year = []    
for i in dates_2:
    month.append(i.month)
    day.append(i.day)
    year.append(i.year)
    
df['day'] = day
df['month'] = month
df['year'] = year

# groups = df.groupby(['month', 'year'])

# print(type(groups['Death rate'].agg(np.mean)))

q1 = """

WITH 
        sum_groups 
        AS (
            SELECT month, year, SUM(Daily_cases) AS MONTHLY_CASES, SUM(Daily_deaths) AS MONTHLY_DEATHS
            FROM df 
            GROUP BY month, year 
            ORDER BY year),
        last_groups 
        AS (
            SELECT df.month, df.year, Deaths, Cases, Active_cases 
            from df INNER JOIN (SELECT month, year, MAX(day) AS day from df GROUP BY month, year) df2 
            ON df.day=df2.day AND df.month=df2.month AND df.year=df2.year)
        
        SELECT last_groups.month, last_groups.year, MONTHLY_CASES, MONTHLY_DEATHS,  Deaths, Cases, Active_cases
 FROM sum_groups INNER JOIN last_groups ON sum_groups.month = last_groups.month AND sum_groups.year = last_groups.year;

"""

df2 = ps.sqldf(q1, locals())
df2.to_csv('covid_Egypt_data_monthly.csv', index=None)

