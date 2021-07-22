import pandas as pd
import numpy as np
from lxml.html import parse, etree
from io import StringIO
# url = 'https://finance.naver.com/item/sise_day.nhn?code=005930'
# data = requests.get(url)
# doc = parse(StringIO(data.text)) # 데이터 계층형구조
fp = open("stock.html").read()
doc = parse(StringIO(fp))
root = doc.getroot() # 제일 상위 테그 html
tables = doc.findall(".//table") # 모든 table tag데이터 추출
titles = tables[0].findall(".//th") # 첫번째 table에서 th태그 전부추출
cols = []
for title in titles:
    cols.append(title.text_content()) # th에 있는 글자 list
values = []
contents = tables[0].findall('.//td')
for content in contents:
    if content.text_content() != '': # 값이 있으면
        values.append((content.text_content().strip()))
ar = np.array(values).reshape(10,7)
df = pd.DataFrame(ar, columns=cols)
print(df)