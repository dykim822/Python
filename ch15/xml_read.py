import pandas as pd
import xml.etree.ElementTree as et
import urllib.request as req
url = 'http://www.kma.go.kr/wid/queryDFS.jsp?gridx=%d&gridy=%d'
reqest = req.Request(url)
response = req.urlopen(reqest)
tree = et.parse(response) # xml형식으로 해석
root = tree.getroot()
k = root.find('body')
items = k.findall('data')
ar = [] # list 생성
for i in items:
    item = {} # dict 생성 키와 값 자바의 map과 유사
    item['temp'] = i.find('temp').text
    item['wfKor']  = i.find('wfKor').text
    ar.append(item)
df = pd.DataFrame(ar, columns=['temp', 'wfKor'])
print(df)