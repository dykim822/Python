from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from nltk import Text
from konlpy.corpus import kolaw
font_path = "c:/Windows/Fonts/malgun.ttf"
data = kolaw.open('constitution.txt').read()
okt = Okt()
nouns = okt.nouns(data)
for noun in nouns:
    if len(noun) < 2:     # 한글자인지 확인
        nouns.remove(noun) # 제거
text = Text(nouns) # 단어별 갯수
data1 = text.vocab() # 단어별 갯수 정리
data100 = data1.most_common(100)
dic = dict(data100)
wc = WordCloud(width=1000, height=600, background_color='white',font_path=font_path)
plt.imshow(wc.generate_from_frequencies(dic))
plt.axis("off")
plt.show()