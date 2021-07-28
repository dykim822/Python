from konlpy.tag import Okt
from collections import Counter
nount_count = 200
result_file_name = 'count.txt'
# dong1에서 저장한 파일명 사용 : a.txt
open_text_file = open('a.txt', 'r', encoding='utf-8')
text = open_text_file.read()
okt = Okt()
# 문장에서 명사만 골라 내라
nouns = okt.nouns(text)
# 명사의 이름과 갯수
# print(nouns)
count = Counter(nouns)
# {명사:갯수, 명사:개수 ,,.....}
# print(count)
tags = []
# n명사 c갯수
for n, c in count.most_common(200):
    temp = {'tag':n, 'count': c}
    tags.append(temp)
open_text_file.close()
# 저장할 파일
open_result_file = open(result_file_name,'w',encoding='utf-8')
for tag in tags:
    noun = tag['tag']
    cnt = tag['count']
    open_result_file.write('{} {}\n'.format(noun, cnt))
open_result_file.close()
print(result_file_name,'에 저장 완료')