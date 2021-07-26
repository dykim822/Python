import pandas as pd
stock1 = {'name': ['다음',"네이버", "넥슨", "NC"],
    '2017-03-20': [84900, 818000, 1756,292000],
    '2017-03-21': [86100, 871000, 1776,295000]}
stock2 = {'name': ['다음',"네이버", "넥슨", "NC"],
    '2017-04-20': [90800, 796000, 1695,366500],
    '2017-04-21': [90600, 806000, 1703,358500]}
df1 = pd.DataFrame(stock1, columns=['name','2017-03-20','2017-03-21'])
df2 = pd.DataFrame(stock2, columns=['name','2017-04-20', '2017-04-21'])
print(df1)
print(df2)
result= df1.merge(df2)
print(result)