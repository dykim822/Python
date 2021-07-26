from bs4 import BeautifulSoup
import urllib.request as req
print('지역코드를 입력하세요')
stdId = input()
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId="+stdId
savename = "forcast.xml"
req.urlretrieve(url, savename) # 인터넷에서 받아서 파일로 저장
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'xml')
info = [] # list
for location in soup.find_all("location"):
    city = {} # dict
    name = location.find("city").string  #city태그 사이의 문자
    datas = location.find_all("data")
    times = []
    for data in datas:
        dt = {}
        tmEf = data.find("tmEf").string
        wf = data.find("wf").string
        dt['tmEf'] = tmEf  # 날자와 시간
        dt["wf"] = wf # 날씨
        times.append(dt)
    city[name] = times
    info.append(city)
print(info) # 여러 도시별 시간때별 날씨
ct1 = ""
for i in info:
    for j in i:
        print("\n", j) # 도시명
        for k in i[j]: # dict 키가 j인 값
            print("|",k['tmEf'],k['wf']) # 시간 날씨
