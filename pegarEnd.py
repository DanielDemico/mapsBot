import pandas as pd

df = pd.read_excel('./Arquivos/fake_addresses.xlsx')


print(df.head())

dataframes = []

for city, group in df.groupby("State"):
    dataframes.append(group)
    
print(dataframes)
print(len(dataframes))
