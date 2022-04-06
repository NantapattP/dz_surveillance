import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

df = pd.read_csv('clean_cow.csv')
df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d', utc=False).dt.date
df.sort_values([ 'Time','Keyword'], inplace=True)
df.drop(columns=['Body','cleaning'], inplace=True)
df.dropna(inplace=True)

FMD = df.loc[df['Keyword'].str.contains('FMD|Foot and mouth disease|ปากและเท้าเปื่อย', regex=True)]
FMD['freq_perday'] = FMD.groupby('Time')['Time'].transform('count')

LSD = df.loc[df['Keyword'].str.contains('ลัมปีสกิน|Lumpy skin disease|LSD', regex=True)]
LSD['freq_perday'] = LSD.groupby('Time')['Time'].transform('count')

All2 = pd.merge(FMD, LSD, left_index=False, right_index=False, how="outer")

Animal_only = df.loc[~(df['Keyword'].isin(All2['Keyword']))]
Animal_only['freq_perday'] = Animal_only.groupby('Time')['Time'].transform('count')

#plot
plt.figure(figsize=(15,5))

plt.plot(FMD.Time, FMD.freq_perday, label='FMD')
plt.plot(LSD.Time, LSD.freq_perday, label='LSD')
plt.plot(Animal_only.Time, Animal_only.freq_perday, label='Animal')

plt.legend()

plt.title('Frequency of each disease per day')
plt.xlabel('Date')
plt.ylabel('Total/day')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.savefig('cow_disease', dpi=300)

plt.show()


# df.to_excel('cow2.xlsx', index=False)