from bs4 import BeautifulSoup
# 분석 대상 HTML
html = """
<html><body>
<div id="meigen">
<h1>위키북스 도서</h1>
<ul class="items">
<li>유니티 게임 이펙트 입문</li>
<li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
<li>모던 웹사이트 디자인의 정석</li>
</ul>
</div>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one('div#meigen > h1').string
print('h1 =', h1)
lists = soup.select("ul.items > li")
for i in lists:
    print('li =', i.string)