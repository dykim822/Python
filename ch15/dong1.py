from bs4 import BeautifulSoup
import urllib.request
# quote url에 한글(utf-8)이 포함되어 있을 때 아스키형식으로 변경
from urllib.parse import quote
print('검색어를 입력하세요')
keyword = input()
# 1페이당 기사 15개
page_num = int(input('페이지 갯수'))
output_file_name = input('저장할 파일명')
output_file = open(output_file_name,'w',encoding='utf-8')
# check_new = 1 뉴스
# more=1 더보기가 누른 상태
# sorting = 3정확도순 정열, range=3 전체기간
for i in range(page_num):
    current_page_num = 1 + i*15
    target_url = "http://news.donga.com/search?p="+\
        str(current_page_num)+"&query="+quote(keyword)+\
        "&check_news=1&more=1&sorting=3&serach_date=1&range=3"
    source_code = urllib.request.urlopen(target_url)
    soup = BeautifulSoup(source_code,'lxml', from_encoding='utf-8')
    print(target_url)
    # print(soup)
    # p태그나 tit를 찾아
    for title in soup.find_all('p','tit'):
        title_link = title.select('a')
        # 연결된 url(인터넷 주소) 자져와서 article_url으로 저장
        article_url = title_link[0]['href']
        source_code_from = urllib.request.urlopen(article_url)
        # soup 첫번째 화면에서 연결된 뉴스
        soup = BeautifulSoup(source_code_from,'lxml',from_encoding='utf-8')
        # <div class=article_txt>뉴스 ....</div>에 있는 일기
        content_of_article = soup.select('div.article_txt')
        print(content_of_article)
        for item in content_of_article:
            string_item = str(item.find_all(text=True))
            output_file.write(string_item)
print(output_file_name,'에 저장 완료')
output_file.close()
