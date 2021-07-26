import pandas as pd
import numpy as np
stock = {
    '2017-03-20': [84900, 1756,292000],
    '2017-03-21': [86100, np.nan,295000]}
df = pd.DataFrame(stock, index=['다음',"넥슨", "NC"])
print(df)
df = df.rename(index={'다음':'DAUM', '넥슨':'NEXON'})
print(df)
print(df.replace({np.nan:'-'}))
