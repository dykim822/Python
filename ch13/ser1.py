import pandas as pd
price = pd.Series([4000, 3000, 3500, 2000])
print(price)
print(price.index)
print(price.values)
price2 = pd.Series([4000, 3000, 3500, 2000], index = ['apple','mellon','orange','kiwi'])
print(price2)
print(price2.index)
print(price2.values)
print(price2[0])
print(price2['apple'])