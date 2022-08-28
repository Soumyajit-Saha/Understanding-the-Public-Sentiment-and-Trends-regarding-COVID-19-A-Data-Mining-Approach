# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:49:15 2022

@author: Soumyajit Saha
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

months = ['Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22']

df = pd.read_csv('covid_world_data_monthly.csv')
df2 = pd.read_csv('covid_World_vaccine_monthly.csv')

df = df.iloc[1:-1 , :]
df2 = df2.iloc[1:-1 , :]

plt.figure(figsize = (10,7))
plt.plot( months, df['Deaths'], linewidth=0.5, color = 'black', label = 'Deaths')
plt.plot( months, df['MONTHLY_CASES'], linewidth=0.5, color = 'blue', label = 'Mothly cases')
plt.plot( months, df['MONTHLY_DEATHS'], linewidth=0.5, color = 'green', label = 'Mothly deaths')
plt.plot( months, df['Cases'], linewidth=0.5, color = 'red', label = 'Cases')
plt.plot( months, df['Active_cases'], linewidth=0.5, color = 'purple', label = 'Active cases')


plt.ylabel("Count")
plt.xlabel("Time Period")
plt.title('Monthly Covid Trends All Over The World', fontsize = 15)
plt.xticks(rotation = 90)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.legend()
plt.show()

plt.plot( months, df['DEATH_RATE'], linewidth=0.5, color = 'red', label = 'Death rate')
plt.plot( months, df['RECOVERY_RATE'], linewidth=0.5, color = 'green', label = 'Recovery rate')


plt.ylabel("Count")
plt.xlabel("Time Period")
plt.title('Monthly Covid Trends All Over The World', fontsize = 15)
plt.xticks(rotation = 90)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.legend()
plt.show()

plt.plot( months, df2['total_boosters'], linewidth=0.5, color = 'red', label = 'Total boosters')
plt.plot( months, df2['total_vaccinations'], linewidth=0.5, color = 'green', label = 'Total vaccinations')
plt.plot( months, df2['people_vaccinated'], linewidth=0.5, color = 'blue', label = 'People vaccinated')
plt.plot( months, df2['people_fully_vaccinated'], linewidth=0.5, color = 'purple', label = 'People fully vaccinated')
plt.plot( months, df2['new_vaccinations'], linewidth=0.5, color = 'cyan', label = 'New vaccinations')





plt.ylabel("Count")
plt.xlabel("Time Period")
plt.title('Monthly Vaccination Trends All Over The World', fontsize = 15)
plt.xticks(rotation = 90)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.legend()
plt.show()

sentiments = [-0.0413, -0.2126, -0.3457, -0.3945, -0.4125, -0.4678, -0.5671, -0.5436, -0.4355, -0.3242, -0.1238, 0.2657, 0.1006, 0.0024, -0.2694, -0.4375, -0.4678, -0.3245, -0.2137, -0.0016, 0.0012, -0.0107, 0.0005, -0.0197, 0.0014]

print('Correlation with Active cases: ', np.corrcoef(df['Active_cases'], sentiments)[0][1])
print('Correlation with Deaths: ', np.corrcoef(df['Deaths'], sentiments)[0][1])
print('Correlation with Monthly Cases: ', np.corrcoef(df['MONTHLY_CASES'], sentiments)[0][1])
print('Correlation with Monthly Deaths: ', np.corrcoef(df['MONTHLY_DEATHS'], sentiments)[0][1])
print('Correlation with Death Rate: ', np.corrcoef(df['DEATH_RATE'], sentiments)[0][1])
print('Correlation with Recovery Rate: ', np.corrcoef(df['RECOVERY_RATE'], sentiments)[0][1])
print('Correlation with Total Boosters: ', np.corrcoef(df2['total_boosters'], sentiments)[0][1])
print('Correlation with Total Vaccinations: ', np.corrcoef(df2['total_vaccinations'], sentiments)[0][1])
print('Correlation with People Vaccinated: ', np.corrcoef(df2['people_vaccinated'], sentiments)[0][1])
print('Correlation with People Fully Vaccinated: ', np.corrcoef(df2['people_fully_vaccinated'], sentiments)[0][1])
print('Correlation with New Vaccinations: ', np.corrcoef(df2['new_vaccinations'], sentiments)[0][1])


plt.plot( months, sentiments, linewidth=0.5, color = 'blue', label = 'Sentiments')


plt.ylabel("Sentiments")
plt.xlabel("Time Period")
plt.title('Sentiments analysed from Twitter Tweets', fontsize = 15)
plt.xticks(rotation = 90)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.legend()
plt.show()

