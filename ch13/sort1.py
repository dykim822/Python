import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three','one'],
                  columns=['d','a','b','c'])
print(df)
print(df.sort_index())
print(df.sort_index(axis=1))
print(df.sort_index(ascending=False, axis=1))