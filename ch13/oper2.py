import pandas as pd
import numpy as np
df2 = pd.DataFrame(np.random.randint(10, size=(4, 8)))
print(df2)
df2["RowSum"] = df2.sum(axis=1)
print(df2)
df2.loc["ColToal",:] = df2.sum()
print(df2)