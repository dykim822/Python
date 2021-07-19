import numpy as np
import pandas as pd
df = pd.DataFrame(np.arange(10,22).reshape(3, 4), index=['a','b','c'],
                  columns=["A","B","C","D"])
print(df)
print(df.iloc[0, 1]) # 0행에 1열
print(df.iloc[:2, 2]) # 인덱스 2앞행중에서 2열
print(df.iloc[:2, -2:]) # 행은 2앞까지 열은 -2열 이상
print(df.iloc[2:3, 1:3]) # 행 2부터 3행 앞(즉 2열) 열은 1열부터 3열 앞(즉 1, 2열)