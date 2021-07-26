import pandas as pd
df = pd.read_csv('tips.csv')
print(df)
gp = df['tip'].groupby(df['time'])
print(gp)
for name, group in gp:
    print(name)
    print(group)
import numpy as np
gp2 = df['tip'].groupby([df['time'], df['sex']])
print(gp2)
result = gp2.mean().unstack()
result = result.replace(np.nan,'-')
print(result)