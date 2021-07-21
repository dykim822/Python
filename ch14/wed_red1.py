import requests
url = "http://www.naver.com"  #"http://www.choongang.co.kr"
data = requests.get(url)
print(data.text)