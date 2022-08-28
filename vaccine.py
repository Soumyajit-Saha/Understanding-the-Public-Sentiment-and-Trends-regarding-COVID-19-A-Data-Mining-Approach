# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 01:25:22 2022

@author: Soumyajit Saha
"""

import pandasql as ps
import pandas as pd
from datetime import datetime

df = pd.read_csv('vaccine-covid-data.csv')

df = df.fillna(0)

dates = df['date'].to_list()

dates_2 = []
for d in dates:
    dates_2.append(datetime.strptime(d, '%Y-%m-%d'))
    
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

q1 = """

SELECT month, year, MAX(total_vaccinations) AS total_vaccinations, MAX(people_vaccinated) AS people_vaccinated, MAX(people_fully_vaccinated) AS people_fully_vaccinated, MAX(total_boosters) AS total_boosters, MAX(new_vaccinations) AS new_vaccinations 
FROM df
GROUP BY month, year
ORDER BY year

"""

df2 = ps.sqldf(q1, locals())
df2.to_csv('covid_World_vaccine_monthly.csv', index=None)
