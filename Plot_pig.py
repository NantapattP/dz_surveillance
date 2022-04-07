import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

df = pd.read_csv('clean_pig.csv')

df.dropna(inplace=True)
df.drop(columns=['Body','cleaning'], inplace=True)

df['Time'] = pd.to_datetime(df['Time']).dt.strftime("%d/%m/%Y %I:%M")
df.Time = df.Time.astype('datetime64')
df.Like = df.Like.astype('int64')
df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d', utc=False).dt.date

df.sort_values([ 'Time','Keyword'], inplace=True)

# df.to_excel('clean_pig.xlsx', encoding='utf-8')


ASF = df.loc[df['Keyword'].str.contains('ASF|African swine fever|อหิวาต์แอฟริกาในสุกร', regex=True)]
ASF['freq_perday'] = ASF.groupby('Time')['Time'].transform('count')

Animal_only = df.loc[~(df['Keyword'].isin(ASF['Keyword']))]
Animal_only['freq_perday'] = Animal_only.groupby('Time')['Time'].transform('count')

#plot
plt.figure(figsize=(15,5))

plt.plot(ASF.Time, ASF.freq_perday, label='ASF')
plt.plot(Animal_only.Time, Animal_only.freq_perday, label='Sick pig')

plt.legend()

plt.title('Frequency of each disease per day')
plt.xlabel('Date')
plt.ylabel('Total/day')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.savefig('pig_disease', dpi=300)

plt.show()