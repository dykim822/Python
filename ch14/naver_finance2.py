# import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
# url = 'https://finance.naver.com/item/sise_day.nhn?code=005930'
# data = requests.get(url)
fp = open("stock.html", 'r').read()
doc = BeautifulSoup(fp, 'html.parser')
tables = doc.select("table") # 모든 table tag데이터 추출
titles = tables[0].select("th") # 첫번째 table에서 th태그 전부추출
cols = []
for title in titles:
    cols.append(title.text) # th에 있는 글자 list
values = []
contents = tables[0].select('td')
# print(contents)
for content in contents:
    if content.text != '': # 값이 있으면
        values.append((content.text.strip()))
ar = np.array(values).reshape(10,7)
df = pd.DataFrame(ar, columns=cols)
print(df)