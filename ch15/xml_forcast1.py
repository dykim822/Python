from bs4 import BeautifulSoup
import urllib.request as req
import os.path
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
save = "forcast.xml"
req.urlretrieve(url, save)
xml = open(save,'r', encoding="utf-8").read()
soup =BeautifulSoup(xml, 'xml')
info = {}  # dictionary생성
for location in soup.find_all("location"):
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info):
        info[weather] = [] # list 생성
    info[weather].append(name)
# 각 지역 날씨를 구분하여 출력하기
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("|-", name)