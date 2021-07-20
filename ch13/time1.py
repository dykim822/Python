import pandas as pd
date_idx = pd.date_range('11/27/2016', periods=5, freq='D')
print(date_idx)
df = pd.DataFrame({"c1":[10, 20,30,40,50]}, index=date_idx)
print(df)
date_idx = pd.date_range('2020-04-01', periods=5, freq='D')
df = pd.DataFrame([10, 20,30,40,50], index=date_idx, columns=['수량'])
print(df)
date_idx2 = pd.date_range('2020-03-28', periods=9, freq='D')
# bfil 4월 1일 이전 데이터 4월 1일 데이터 채운다
df = df.reindex(date_idx2, method='bfill')
print(df)
date_idx3 = pd.date_range('2020-03-28', periods=12, freq='D')
# bfil 4월 1일 이전 데이터 4월 1일 데이터 채운다
df = df.reindex(date_idx3, method='ffill')
print(df)