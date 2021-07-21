from bs4 import BeautifulSoup
# 분석하고 싶은 HTML
html = """
<html><body>
<h1>스크레이핑이란?</h1>
<p>웹 페이지를 분석하는 것</p>
<p>원하는 부분을 추출하는 것</p>
</body></html>
"""
# html문서로 분석
soup = BeautifulSoup(html,'html.parser')
h1 = soup.html.body.h1
p1 = soup.html.body.p
# 같은 레벨의 다음 데이터
p2 = p1.next_sibling.next_sibling
print("h1 =", h1.string)
print("p1 =", p1.string)
print("p2 =", p2.string)

