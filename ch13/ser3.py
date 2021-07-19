import pandas as pd
# 2015년 인구
s1 = pd.Series([9904312,3448737,2890451, 2466052], index=['서울','부산','인천','대구'])
print(s1)
# 2010년 인구 dictionary로도 Series만든다
s2 = pd.Series({'서울':9631482,'부산':3393191,'인천':2632035,'대전':1490158})
print(s2)
ds = s1 - s2
print(ds)
rs = (s1 - s2)/s2 * 100
print(rs)
print(rs[rs.notnull()])