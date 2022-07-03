import pandas as pd



df = pd.read_csv('data_csv_all_points_noDNSqueries.csv')
print(df)

print(df.loc[df['Blacklisted'] == 0].mean() - df.loc[df['Blacklisted'] == 1].mean())
