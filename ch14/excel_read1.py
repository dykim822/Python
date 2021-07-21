import pandas as pd
f = pd.ExcelFile('excel.xlsx')
df = f.parse("Sheet1",index_col=0 )
print(df)
print("==============")
df2 = pd.read_excel('excel.xlsx',"Sheet1",index_col=0)
print(df2)