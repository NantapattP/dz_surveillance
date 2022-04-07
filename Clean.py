import pandas as pd
df = pd.read_csv('BlueEyeExportDemo Account 1-20220323205407.csv', encoding='utf-16-le', sep='\t')
#df.columns

df = df.drop(columns=['Msg ID', 'Sentiment', 'Text', 'Author'])

#seperate 2 df
#cow df
df = df.loc[(df['Keyword'] == 'ลัมปีสกิน') | (df['Keyword'] == 'Lumpy skin disease') | (df['Keyword'] == 'วัวป่วย') | (df['Keyword'] == 'FMD')| (df['Keyword'] == 'Foot and mouth disease') | (df['Keyword'] == 'ปากและเท้าเปื่อย')]
df.drop_duplicates('Body', inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)

# df.to_csv('cattle.csv', index=False)


#pig df
new_df = df.loc[(df['Keyword'] == 'ASF') | (df['Keyword'] == 'African swine fever') | (df['Keyword'] == 'อหิวาต์แอฟริกาในสุกร') | (df['Keyword'] == 'หมูป่วย')]
new_df.drop_duplicates('Body', inplace=True)
new_df.reset_index(inplace =True, drop=True)
print(new_df)

# new_df.to_csv('pig.csv', index=False)

