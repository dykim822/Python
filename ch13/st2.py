import pandas as pd
import numpy as np
stocks = {'2017-02-19':{'다음':50300,"네이버": 51100},
"2017-02-22":{'다음':50300, '네이버': 50800},
'2016-02-23':{'다음':50800,'네이버': 53000}}
data = pd.DataFrame(stocks).T
print(data)
print(data.diff())
print(data.pct_change())