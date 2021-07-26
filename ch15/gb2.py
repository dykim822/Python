import pandas as pd
df = pd.read_csv('tips.csv', index_col='sex')
print(df)
# Female 6, Male 4
print(df.groupby(len).mean())