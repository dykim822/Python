import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(10,22).reshape(3, 4), index=['a','b','c'],
                  columns=["A","B","C","D"])
print(df)
print(df.loc['a'])   # dataframe형식 유지 안함
print(df.loc[['a']]) # dataframe형식 유지
print(df.loc['b':'c'])
print(df.loc['b':'c'])
print(df.loc['a',"A"])
print(df.loc[['a','b'],["B","D"]])
print(df.loc[df.A > 10,["C","D"]])